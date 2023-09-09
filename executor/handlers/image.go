package handlers

import (
	"executor/db"
	"executor/docker"
	"executor/models"
	"fmt"
	"net/http"
	"sync"

	"github.com/gorilla/websocket"
	"github.com/labstack/echo/v4"
	"github.com/rs/zerolog/log"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

func CreateImage(c echo.Context) error {

	ws, err := upgrader.Upgrade(c.Response(), c.Request(), nil)
	if err != nil {
		return err
	}
	defer ws.Close()
	type RequestBody struct {
		ImageName  string `json:"ImageName"`
		Tag        string `json:"Tag"`
		Dockerfile string `json:"Dockerfile"`
		UserID     string `json:"user_id"` // This is just a temporary thing
	}
	var req RequestBody
	ws.ReadJSON(&req)
	var wg sync.WaitGroup
	ch := make(chan models.Response)

	go docker.BuildImage(req.ImageName, req.Tag, req.Dockerfile, req.UserID, ch, &wg)
	for {
		resp := <-ch
		fmt.Println(resp)
		if resp.Message == "building" {
			data := map[string]interface{}{
				"status": "building",
			}
			ws.WriteJSON(data)
		} else {
			if resp.Success {
				data := map[string]interface{}{
					"status":  "finished",
					"imgName": resp.Message,
				}
				ws.WriteJSON(data)
			} else {
				data := map[string]interface{}{
					"status":  "finished",
					"imgName": resp.Message,
				}
				ws.WriteJSON(data)
			}
			break
		}

	}
	return nil
}

func DeleteImage(c echo.Context) error {
	userID := c.Request().Context().Value("UserID").(string)

	type RequestBody struct {
		ID        string `json:"ID"`
		ImageName string `json:"ImageName"`
		Tag       string `json:"Tag"`
	}

	requestBody := new(RequestBody)

	if err := c.Bind(requestBody); err != nil {
		return err
	}
	imageName := fmt.Sprintf("%s-%s:%s", requestBody.ImageName, userID, requestBody.Tag)
	err := db.DeleteImageByID(requestBody.ID)
	if err != nil {
		log.Error().Str("Error", err.Error())
		data := map[string]interface{}{
			"success": false,
			"error":   err.Error(),
		}
		return c.JSON(http.StatusInternalServerError, data)
	}
	_, err = docker.DeleteImage(imageName)
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
