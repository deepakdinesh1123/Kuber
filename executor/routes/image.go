package routes

import (
	"executor/handlers"

	"github.com/labstack/echo/v4"
)

func RegisterImageRoutes(e *echo.Echo) {
	e.GET("/image/build", handlers.CreateImage)
	e.DELETE("/image", handlers.DeleteImage)
}
