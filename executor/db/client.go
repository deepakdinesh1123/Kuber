package db

import (
	"fmt"
	"sync"

	"github.com/spf13/viper"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var once sync.Once

type DriverPg struct {
	DB *gorm.DB
}

// variavel Global
var Postgres *DriverPg

func Connect() *DriverPg {

	once.Do(func() {
		host, _ := viper.Get("DB_HOST").(string)
		db_name, _ := viper.Get("DB_NAME").(string)
		user, _ := viper.Get("DB_USER").(string)
		password, _ := viper.Get("DB_PASSWORD").(string)
		port, _ := viper.Get("DB_PORT").(string)
		dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=disable TimeZone=Asia/Shanghai", host, user, password, db_name, port)
		db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
		if err != nil {
			panic(err)
		}
		Postgres = &DriverPg{DB: db}
	})

	return Postgres
}
