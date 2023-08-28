package db

import (
	"sync"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var once sync.Once

type DriverPg struct {
	DB *gorm.DB
}

// variavel Global
var instance *DriverPg

func Connect() *DriverPg {

	once.Do(func() {
		dsn := "host=your-hostname user=your-username password=your-password dbname=your-dbname port=5432 sslmode=disable TimeZone=Asia/Shanghai"
		db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
		if err != nil {
			panic(err)
		}
		instance = &DriverPg{DB: db}
	})

	return instance
}
