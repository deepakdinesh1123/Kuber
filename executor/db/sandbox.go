package db

import (
	"time"

	"github.com/google/uuid"
	"gorm.io/datatypes"
)

type Containers struct {
	Containers []string `json:"containers"`
}

type Sandbox struct {
	ID         uuid.UUID      `gorm:"column:id"`
	CreatedAt  time.Time      `gorm:"column:created_at"`
	Name       string         `gorm:"column:name"`
	Private    bool           `gorm:"column:private"`
	Containers datatypes.JSON `gorm:"column:containers"`
	EnvID      uuid.UUID      `gorm:"column:env_id"`
	CreatorID  uuid.UUID      `gorm:"column:creator_id"`
	Running    bool           `gorm:"column:running"`
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

func CreateNewSandbox(private bool, EnvID, creatorID, Name, containers string) error {
	envUUID, err := uuid.Parse(EnvID)
	if err != nil {
		return err
	}
	creatorUUID, err := uuid.Parse(creatorID)
	if err != nil {
		return err
	}
	sandbox := Sandbox{ID: uuid.New(), CreatedAt: time.Now(), Private: private, EnvID: envUUID, CreatorID: creatorUUID, Running: true}
	sandbox.Containers = datatypes.JSON([]byte(containers))
	res := Postgres.DB.Create(&sandbox)
	if res.Error != nil {
		return res.Error
	}
	return nil
}
