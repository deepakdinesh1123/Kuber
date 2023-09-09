package handlers

import (
	"executor/db"
	"executor/docker"
	"executor/models"
	"net/http"

	"github.com/labstack/echo/v4"
)

func CreateSandbox(c echo.Context) error {

	userID := c.Request().Context().Value("UserID").(string)
	type RequestBody struct {
		SandboxName   string `json:"SandboxName"`
		SandboxType   string `json:"SandboxType"`
		ProjectName   string `json:"ProjectName"`
		ImageName     string `json:"ImageName"`
		EnvironmentID string `json:"EnvironmentID"`
		Private       bool   `json:"Private"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	containerConfig := docker.EmptyContainerConfig()

	sandboxconfig := docker.NewSandboxConfig(containerConfig)

	sandbox := docker.NewSandbox(requestBody.SandboxName, requestBody.SandboxType, requestBody.ProjectName, requestBody.EnvironmentID, requestBody.ImageName, sandboxconfig)

	container, err := sandbox.CreateSandbox()

	if err != nil {
		data := map[string]interface{}{
			"success": false,
			"message": "could not create sandbox",
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	containers := models.JSONB{"containers": []string{container.ContainerName}}
	err = db.CreateNewSandbox(requestBody.Private, requestBody.EnvironmentID, userID, requestBody.SandboxName, containers)
	if err != nil {
		data := map[string]interface{}{
			"success": false,
			"message": err.Error(),
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	data := map[string]interface{}{
		"success":     true,
		"container":   container.ContainerName,
		"containerID": container.ID,
	}
	return c.JSON(http.StatusOK, data)

}

func DeleteSandbox(c echo.Context) error {
	sandboxID := c.Param("id")
	sandbox := docker.ExistingSandbox(sandboxID)
	err := sandbox.Delete()
	if err != nil {
		data := map[string]interface{}{
			"success": false,
			"message": err.Error(),
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	data := map[string]interface{}{
		"success": true,
	}
	return c.JSON(http.StatusOK, data)
}
