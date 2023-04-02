package container

import (
	context "context"

	"github.com/docker/docker/api/types/container"
	"github.com/docker/docker/client"
)

type Server struct {
	UnimplementedContainersServer
	DockerClient *client.Client
}

func (s *Server) CreateContainer(ctx context.Context, in *Container) (*ContainerCreationResponse, error) {

	config := &container.Config{
		Image: "alpine:latest",
		Tty:   true,
	}
	res, err := s.DockerClient.ContainerCreate(
		context.Background(),
		config,
		nil,
		nil,
		nil,
		"Test",
	)
	if err != nil {
		return &ContainerCreationResponse{
			Response: &ContainerCreationResponse_ContainerError{
				ContainerError: &ContainerCreationError{
					Error: err.Error(),
				},
			},
		}, err
	}
	return &ContainerCreationResponse{
		Response: &ContainerCreationResponse_ContainerCreated{
			ContainerCreated: &ContainerCreated{
				Name: res.ID,
			},
		},
	}, err
}
