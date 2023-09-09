package db

import (
	"fmt"
	"time"

	"executor/models"

	"github.com/google/uuid"
	"gorm.io/gorm"
)

type Containers struct {
	Containers []string `json:"containers"`
}

type Sandbox struct {
	ID         uuid.UUID    `gorm:"column:id"`
	CreatedAt  time.Time    `gorm:"column:created_at"`
	Name       string       `gorm:"column:name"`
	Private    bool         `gorm:"column:private"`
	Containers models.JSONB `gorm:"type:jsonb" column:"containers"`
	EnvID      uuid.UUID    `gorm:"column:env_id"`
	CreatorID  uuid.UUID    `gorm:"column:creator_id"`
	Running    bool         `gorm:"column:running"`
}

func (Sandbox) TableName() string {
	return "environment_sandbox"
}

func GetAllSandboxes() ([]Sandbox, error) {
	var sandboxes []Sandbox
	if err := Postgres.DB.Find(&sandboxes).Error; err != nil {
		return nil, err
	}
	return sandboxes, nil
}

func CreateNewSandbox(private bool, EnvID, creatorID, Name string, containers models.JSONB) error {
	envUUID, err := uuid.Parse(EnvID)
	if err != nil {
		return err
	}
	creatorUUID, err := uuid.Parse(creatorID)
	if err != nil {
		return err
	}
	sandbox := Sandbox{ID: uuid.New(), CreatedAt: time.Now(), Private: private, EnvID: envUUID, CreatorID: creatorUUID, Running: true, Name: Name}
	sandbox.Containers = containers
	res := Postgres.DB.Create(&sandbox)
	if res.Error != nil {
		return res.Error
	}
	return nil
}

func GetSandboxByID(sandboxID string) (*Sandbox, error) {
	var sandbox Sandbox
	if err := Postgres.DB.Where("id = ?", sandboxID).First(&sandbox).Error; err != nil {
		return nil, err
	}
	if err := Postgres.DB.Model(&sandbox).Select("containers").Where("id = ?", sandboxID).Scan(&sandbox.Containers).Error; err != nil {
		return nil, err
	}
	return &sandbox, nil
}

func DeleteSandboxByID(sandboxID string) error {
	sandboxUUID, err := uuid.Parse(sandboxID)
	if err != nil {
		return err
	}
	sandbox := Sandbox{ID: sandboxUUID}
	result := Postgres.DB.Delete(&sandbox)
	if result.Error != nil {
		fmt.Println("DB", result.Error.Error())
		return result.Error
	}

	// Check if any records were affected
	if result.RowsAffected == 0 {
		return gorm.ErrRecordNotFound // Image with the given ID not found
	}

	return nil
}
