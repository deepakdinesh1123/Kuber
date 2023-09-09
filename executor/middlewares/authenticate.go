package middlewares

import (
	"net/http"
	"strings"

	"github.com/dgrijalva/jwt-go"
	"github.com/labstack/echo/v4"
	"github.com/spf13/viper"
	"golang.org/x/net/context"
)

func TokenMiddleware() echo.MiddlewareFunc {
	return func(next echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			if strings.Contains(c.Request().URL.Path, "swagger") {
				return next(c)
			}
			// Get the token from the request headers
			auth_token := c.Request().Header.Get("Authorization")

			if auth_token == "" {
				return echo.NewHTTPError(http.StatusUnauthorized, "Missing token")
			}

			const bearerPrefix = "Bearer "
			if len(auth_token) <= len(bearerPrefix) || auth_token[:len(bearerPrefix)] != bearerPrefix {
				return echo.NewHTTPError(http.StatusUnauthorized, "Invalid token format")
			}

			// Extract the token payload
			jwt_token := auth_token[len(bearerPrefix):]
			claims := jwt.MapClaims{}
			token, err := jwt.ParseWithClaims(jwt_token, claims, func(t *jwt.Token) (interface{}, error) {
				return []byte(viper.Get("JWT_SECRET_KEY").(string)), nil
			})

			if err != nil || !token.Valid {
				return echo.NewHTTPError(http.StatusUnauthorized, "Invalid token")
			}

			var UserID string

			for key, val := range claims {
				if key == "user_id" {
					UserID = val.(string)
				}
			}

			ctx := context.WithValue(c.Request().Context(), "UserID", UserID)
			c.SetRequest(c.Request().WithContext(ctx))

			return next(c)
		}
	}
}