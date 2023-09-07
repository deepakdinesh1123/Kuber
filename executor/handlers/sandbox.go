package handlers

import (
	"executor/db"
	"executor/docker"
	"fmt"
	"net/http"

	"github.com/labstack/echo/v4"
)

// @Summary Create sandbox
// @Description Creates a sandbox using the specified environment
// @ID get-item-list
// @Accept  json
// @Produce  json
// @Success 200
// @Router /items [get]
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
		return c.String(http.StatusInternalServerError, "Could not create sandbx")
	}

	err = db.CreateNewSandbox(requestBody.Private, requestBody.EnvironmentID, userID, requestBody.SandboxName, "{}")

	return c.String(http.StatusOK, fmt.Sprintf("container: %s", container.ContainerName))

}
