package routes

import (
	"executor/handlers"

	"github.com/labstack/echo/v4"
)

func RegisterImageRoutes(e *echo.Echo) {
	e.POST("/image/build", handlers.CreateImage)
	e.DELETE("/image", handlers.DeleteImage)
}
