package routes

import (
	"executor/handlers"

	"github.com/labstack/echo/v4"
)

func RegisterFileRoutes(e *echo.Echo) {
	e.POST("/", handlers.CreateImage)
}
