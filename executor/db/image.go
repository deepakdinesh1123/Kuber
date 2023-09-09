package db

import (
	"fmt"
	"time"

	"github.com/google/uuid"
	"gorm.io/gorm"
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
	fmt.Println("db", userID)
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

func DeleteImageByID(imageID string) error {
	imageUUID, err := uuid.Parse(imageID)
	if err != nil {
		return err
	}
	image := Image{ID: imageUUID}
	result := Postgres.DB.Delete(&image)
	if result.Error != nil {
		return result.Error
	}

	// Check if any records were affected
	if result.RowsAffected == 0 {
		return gorm.ErrRecordNotFound // Image with the given ID not found
	}

	return nil
}
