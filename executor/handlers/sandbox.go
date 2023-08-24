package handlers

import (
	"executor/docker"
	"fmt"
	"net/http"

	"github.com/labstack/echo/v4"
)

func CreateSandbox(c echo.Context) error {

	type RequestBody struct {
		SandboxName     string `json:"SandboxName"`
		SandboxType     string `json:"SandboxType"`
		ProjectName     string `json:"ProjectName"`
		ImageName       string `json:"ImageName"`
		EnvironmentName string `json:"EnvironmentName"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	containerConfig := docker.EmptyContainerConfig()

	sandboxconfig := docker.NewSandboxConfig(containerConfig)

	sandbox := docker.NewSandbox(requestBody.SandboxName, requestBody.SandboxType, requestBody.ProjectName, requestBody.EnvironmentName, requestBody.ImageName, sandboxconfig)

	container, err := sandbox.CreateSandbox()

	if err != nil {
		return c.String(http.StatusInternalServerError, "Could not create sandbx")
	}

	return c.String(http.StatusOK, fmt.Sprintf("container: %s", container.ContainerName))

}
