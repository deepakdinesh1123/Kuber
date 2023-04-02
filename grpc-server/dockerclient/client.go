package dockerclient

import (
	"github.com/docker/docker/client"
)

func CreateClient() (*client.Client, error) {
	docker_client, err := client.NewClientWithOpts(client.FromEnv)
	if err != nil {
		panic(err)
	}
	return docker_client, nil
}
