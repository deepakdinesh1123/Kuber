package main

import (
	"log"

	"executor/db"
	"executor/routes"

	"executor/middlewares"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/spf13/viper"
)

func main() {

	viper.SetConfigFile(".env")

	err := viper.ReadInConfig()
	if err != nil {
		log.Fatalf("Check your environment variables")
	}

	db.Connect()
	e := echo.New()
	e.Use(middleware.CORS())
	e.Use(middleware.Logger())
	e.Use(middlewares.TokenMiddleware())
	routes.RegisterImageRoutes(e)
	routes.RegisterSandboxRoutes(e)
	routes.RegisterFileRoutes(e)
	e.Logger.Fatal(e.Start(":1323"))
}
