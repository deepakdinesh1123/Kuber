package main

import (
	"bytes"
	"fmt"
	"log"
	"net/http"
	"time"

	"executor/docker"
	"executor/routes"

	_ "executor/docs"

	"github.com/flynn/go-shlex"
	"github.com/gorilla/websocket"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/spf13/viper"
	echoSwagger "github.com/swaggo/echo-swagger"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

func execute(c echo.Context) error {
	ws, err := upgrader.Upgrade(c.Response(), c.Request(), nil)
	if err != nil {
		return err
	}
	defer ws.Close()

	_, command, err := ws.ReadMessage()
	if err != nil {
		log.Println(err)
		return err
	}

	cmd_split, err := shlex.Split(string(command))
	if err != nil {
		ws.WriteMessage(websocket.TextMessage, []byte("check cmd"))
		return err
	}

	proc := docker.NewProcess("nerdy-fuchsia-spider", cmd_split, "/")
	err = proc.Start()
	if err != nil {
		log.Println(err)
		return err
	}
	fmt.Println("Process started")

	pid, err := proc.GetPID()
	if err != nil {
		ws.WriteMessage(websocket.TextMessage, []byte("failed"))
		return err
	}
	a := fmt.Sprintf("pid is %s", pid)
	var buffer bytes.Buffer
	buffer.WriteString(a)
	ws.WriteMessage(websocket.TextMessage, buffer.Bytes())

	for {
		// Read
		_, input, err := ws.ReadMessage()
		if err != nil {
			ws.WriteMessage(websocket.TextMessage, []byte("check inp"))
			return err
		}

		switch string(input) {
		case "read":
			if !proc.IsAlive() {
				out, err := proc.ReadOutput()
				if err != nil {
					ws.WriteMessage(websocket.TextMessage, []byte("read out error"))
				}
				ws.WriteMessage(websocket.TextMessage, []byte(out))
				ws.Close()
			} else {
				timeout := time.Second
				out, err := proc.ReadLineWithTimeout(timeout)
				if err != nil {
					ws.WriteMessage(websocket.TextMessage, []byte("some error"))
					return err
				}
				ws.WriteMessage(websocket.TextMessage, []byte(out))
			}
		default:
			err := proc.WriteInput(string(input))
			if err != nil {
				ws.WriteMessage(websocket.TextMessage, []byte("write error"))
			}
		}
	}
}

// @title		Executor API
// @version		0.1.0
// @description	This is the REST API for the executor
// @termsOfService	http://swagger.io/terms/
func main() {

	viper.SetConfigFile(".env")

	err := viper.ReadInConfig()
	if err != nil {
		log.Fatalf("Check your environment variables")
	}

	e := echo.New()
	e.Use(middleware.CORS())
	e.Use(middleware.Logger())
	routes.RegisterImageRoutes(e)
	routes.RegisterSandboxRoutes(e)
	e.GET("/swagger/*", echoSwagger.WrapHandler)
	e.GET("/ws", execute)
	e.Logger.Fatal(e.Start(":1323"))
}
