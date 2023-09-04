package middleware

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"golang.org/x/net/context"
)

func TokenMiddleware(next echo.HandlerFunc) echo.HandlerFunc {
	return func(c echo.Context) error {
		// Get the token from the request headers
		token := c.Request().Header.Get("Authorization")

		if token == "" {
			return echo.NewHTTPError(http.StatusUnauthorized, "Missing token")
		}

		// Here, you can implement your token validation logic.
		// For simplicity, we'll assume the token format is "Bearer <token>"
		// and we'll extract the payload after "Bearer ".
		const bearerPrefix = "Bearer "
		if len(token) <= len(bearerPrefix) || token[:len(bearerPrefix)] != bearerPrefix {
			return echo.NewHTTPError(http.StatusUnauthorized, "Invalid token format")
		}

		// Extract the token payload
		payload := token[len(bearerPrefix):]

		// You can now parse the payload, e.g., decode it from JWT or other formats
		// For this example, we'll just add the payload to the request context as a string.
		ctx := context.WithValue(c.Request().Context(), "tokenPayload", payload)
		c.SetRequest(c.Request().WithContext(ctx))

		// Call the next middleware or route handler
		return next(c)
	}
}
