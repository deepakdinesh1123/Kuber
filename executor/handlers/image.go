package handlers

import (
	"executor/docker"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/rs/zerolog/log"
)

func CreateImage(c echo.Context) error {

	type RequestBody struct {
		ImageName  string `json:"ImageName"`
		Tag        string `json:"Tag"`
		Dockerfile string `json:"Dockerfile"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	_, imgName, err := docker.BuildImage(requestBody.ImageName, requestBody.Tag, requestBody.Dockerfile)
	if err != nil {
		log.Error().Str("Error", err.Error())
		data := map[string]interface{}{
			"success": false,
			"error":   err.Error(),
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	data := map[string]interface{}{
		"success":   true,
		"ImageName": imgName,
	}
	return c.JSON(http.StatusOK, data)
}
