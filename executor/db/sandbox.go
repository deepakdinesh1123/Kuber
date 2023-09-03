package db

import (
	"time"

	"github.com/google/uuid"
	"gorm.io/datatypes"
)

type Sandbox struct {
	ID               int            `gorm:"column:id"`
	CreatedAt        time.Time      `gorm:"column:created_at"`
	Name             string         `gorm:"column:name"`
	Private          bool           `gorm:"column:private"`
	Containers       datatypes.JSON `gorm:"column:containers"`
	EnvID            uuid.UUID      `gorm:"column:env_id"`
	SandboxCreatorID uuid.UUID      `gorm:"column:sandbox_creator_id"`
	UserID           uuid.UUID      `gorm:"column:user_id"`
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
