package handlers

import (
	"executor/docker"
	"fmt"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/rs/zerolog/log"
)

// @Summary Create an image
// @Description Create a Docker image based on the provided parameters.
// @Tags Images
// @Accept json
// @Produce json
// @Param ImageName body string true "Name of the Docker image"
// @Param Tag body string true "Tag for the Docker image"
// @Param Dockerfile body string true "Content of the Dockerfile"
// @Success 200 {object} map[string]interface{} "{success: true, message: "ImageName"}"
// @Failure 500 {object} map[string]interface{} "{success: false, message: "Error"}"
// @Router /images [post]
func CreateImage(c echo.Context) error {

	userID := c.Request().Context().Value("UserID").(string)

	type RequestBody struct {
		ImageName  string `json:"ImageName"`
		Tag        string `json:"Tag"`
		Dockerfile string `json:"Dockerfile"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	_, imgName, err := docker.BuildImage(requestBody.ImageName, requestBody.Tag, requestBody.Dockerfile, userID)
	if err != nil {
		log.Error().Str("Error", err.Error())
		data := map[string]interface{}{
			"success": false,
			"error":   err.Error(),
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	data := map[string]interface{}{
		"success": true,
		"message": imgName,
	}
	return c.JSON(http.StatusOK, data)
}

// @Summary Delete an image
// @Description Delete a Docker image by name and tag.
// @Tags Images
// @Accept json
// @Produce json
// @Param UserID header string true "User ID"
// @Param ImageName body string true "Name of the Docker image"
// @Param Tag body string true "Tag for the Docker image"
// @Success 200 {object} map[string]interface{} "{success: true, message: "ImageName"}"
// @Failure 500 {object} map[string]interface{} "{success: false, message: "Error"}"
// @Router /images/delete [delete]
func DeleteImage(c echo.Context) error {
	userID := c.Request().Context().Value("UserID").(string)

	type RequestBody struct {
		ImageName string `json:"ImageName"`
		Tag       string `json:"Tag"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}
	imageName := fmt.Sprintf("%s-%s:%s", requestBody.ImageName, userID, requestBody.Tag)
	_, err := docker.DeleteImage(imageName)
	if err != nil {
		log.Error().Str("Error", err.Error())
		data := map[string]interface{}{
			"success": false,
			"error":   err.Error(),
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	data := map[string]interface{}{
		"success": true,
		"message": imageName,
	}
	return c.JSON(http.StatusOK, data)
}
