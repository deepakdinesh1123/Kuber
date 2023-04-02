package main

import (
	"fmt"
	"log"
	"net"

	"github.com/deepakdinesh1123/kuber/grpc-server/dockerclient"
	"github.com/deepakdinesh1123/kuber/grpc-server/protos/container"
	"github.com/deepakdinesh1123/kuber/grpc-server/protos/execution"
	"github.com/deepakdinesh1123/kuber/grpc-server/server"
)

func main() {

	docker_client, err := dockerclient.CreateClient()

	listener, err := net.Listen("tcp", "0.0.0.0:9090")
	if err != nil {
		panic(err)
	}

	s, error := server.NewServer()
	if err != nil {
		fmt.Printf("Failed to start server due to error %s", error)
	}
	fmt.Println("Server started")
	execution.RegisterExecuteServer(s, &execution.Server{
		DockerClient: docker_client,
	})
	container.RegisterContainersServer(s, &container.Server{
		DockerClient: docker_client,
	})
	if err := s.Serve(listener); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
