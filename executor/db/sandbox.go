package db

import (
	"time"

	"gorm.io/gorm"
)

type Sandbox struct {
	gorm.Model
	ID        int       `gorm:"column:id"`
	CreatedAt time.Time `gorm:"column:created_at"`
	Private   bool      `gorm:"column:private"`
}
