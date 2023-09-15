package handlers

import (
	"executor/docker"
	"fmt"
	"net/http"

	"github.com/labstack/echo/v4"
)

func CreateFolder(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FolderPath    string `json:"FolderPath"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.CreateFolder(requestBody.FolderPath)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("Folder created\nout: %s", out))
}

func DeleteFolder(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FolderPath    string `json:"FolderPath"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.DeleteFolder(requestBody.FolderPath)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("Folder deleted\nout: %s", out))
}

func GetFolder(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FolderPath    string `json:"FolderPath"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.GetFolderContents(requestBody.FolderPath)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("Folder contents\nout: %s", out))
}

func UpdateFile(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FilePath      string `json:"FilePath"`
		FileContent   string `json:"FileContent"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.UpdateFile(requestBody.FilePath, requestBody.FileContent)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("File Updated\nout: %s", out))
}

func GetFile(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FilePath      string `json:"FilePath"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.GetFile(requestBody.FilePath)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("out: %s", out))
}

func CreateFile(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FilePath      string `json:"FilePath"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.CreateFile(requestBody.FilePath)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("File Created\nout: %s", out))
}

func DeleteFile(c echo.Context) error {

	type RequestBody struct {
		ContainerName string `json:"ContainerName"`
		FilePath      string `json:"FilePath"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}

	container := docker.ExistingContainer(requestBody.ContainerName)
	out, err := container.DeleteFile(requestBody.FilePath)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
	}
	return c.String(http.StatusOK, fmt.Sprintf("File created\nout: %s", out))
}
