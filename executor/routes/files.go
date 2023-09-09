package routes

import (
	"executor/handlers"

	"github.com/labstack/echo/v4"
)

func RegisterFileRoutes(e *echo.Echo) {
	e.POST("/container/file/create", handlers.CreateFile)
	e.POST("/container/file", handlers.UpdateFile)
	e.DELETE("/container/file", handlers.DeleteFile)
}
