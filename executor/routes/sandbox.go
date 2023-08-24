package routes

import (
	"executor/handlers"

	"github.com/labstack/echo/v4"
)

func RegisterSandboxRoutes(e *echo.Echo) {
	e.POST("/sandbox", handlers.CreateSandbox)
}
