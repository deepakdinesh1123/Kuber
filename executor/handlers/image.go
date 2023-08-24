package handlers

import (
	"executor/docker"
	"fmt"
	"net/http"

	"github.com/labstack/echo/v4"
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

	out, imgName, err := docker.BuildImage(requestBody.ImageName, requestBody.Tag, requestBody.Dockerfile)
	if err != nil {
		return c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("out:%s\nImageName:%s", out, imgName))
}
