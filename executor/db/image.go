package db

import (
	"time"

	"github.com/google/uuid"
)

type Image struct {
	ID         uuid.UUID `gorm:"column:id"`
	CreatedAt  time.Time `gorm:"column:created_at"`
	UpdatedAt  time.Time `gorm:"column:updated_at"`
	Name       string    `gorm:"column:name"`
	Dockerfile string    `gorm:"column:Dockerfile"`
	Private    bool      `gorm:"column:private"`
	CreatedBy  uuid.UUID `gorm:"column:created_by_id"`
}

func (Image) TableName() string {
	return "environment_dockerimage"
}

func CreateNewImage(imageName, dockerfile, userID string) error {
	userUUID, err := uuid.Parse(userID)
	if err != nil {
		return err
	}
	image := Image{ID: uuid.New(), Name: imageName, Dockerfile: dockerfile, CreatedBy: userUUID}
	image.CreatedAt = time.Now()
	image.UpdatedAt = time.Now()
	image.Private = true
	res := Postgres.DB.Create(&image)
	if res.Error != nil {
		return res.Error
	}
	return nil
}
