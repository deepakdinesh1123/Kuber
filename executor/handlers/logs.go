package handlers

// import (
// 	"encoding/json"
// 	"executor/docker"
// 	"net/http"
// 	"time"

// 	"github.com/labstack/echo/v4"
// )

// func GetContainerLogs(c echo.Context) error {
// 	type RequestBody struct {
// 		ContainerName string `json:"ContainerName"`
// 	}

// 	requestBody := new(RequestBody)

// 	if err := c.Bind(requestBody); err != nil {
// 		return err
// 	}

// 	containerLogs := make(chan string)

// }
