package docker

import (
	"fmt"
	"os/exec"

	"executor/models"

	"github.com/rs/zerolog/log"
)

type ContainerConfig struct {
	port    *int
	volumes *[]string
}

type Container struct {
	ContainerName string
	ImageName     string
	ID            string
	Config        *ContainerConfig
}

func EmptyContainerConfig() ContainerConfig {
	return ContainerConfig{
		port:    nil,
		volumes: nil,
	}
}

func NewContainerConfig(port int, volumes []string) *ContainerConfig {
	return &ContainerConfig{
		port:    &port,
		volumes: &volumes,
	}
}

func NewContainer(ContainerName, ImageName string, Config ContainerConfig) *Container {
	return &Container{
		ContainerName: ContainerName,
		ImageName:     ImageName,
		Config:        &Config,
	}
}

func ExistingContainer(ContainerName string) *Container {
	return &Container{
		ContainerName: ContainerName,
		ImageName:     "",
		Config:        nil,
	}
}

func (c *Container) CreateContainer() (string, error) {
	log.Debug().Msg(c.ImageName)

	cmd := exec.Command("docker", "run", fmt.Sprintf("--name=%s", c.ContainerName), "-d", "-it", c.ImageName)
	out, err := cmd.Output()
	if err != nil {
		fmt.Println("Error creating container:", err)
		return "", err
	}
	c.ID = string(out)
	return "Container created", nil
}

func (c *Container) StopContainer() error {
	cmd := exec.Command("docker", "stop", c.ContainerName)
	_, err := cmd.Output()
	if err != nil {
		fmt.Println("stop:", err.Error())
		return err
	}
	return nil
}

func (c *Container) DeleteContainer() error {
	cmd := exec.Command("docker", "rm", c.ContainerName)
	_, err := cmd.Output()
	if err != nil {
		fmt.Println("Delete:", err.Error())
		return err
	}
	return nil
}

func (c *Container) IsContainerRunning() models.Response {
	cmdArgs := []string{"inspect", "--format", "'{{json .State.Running}}'", c.ContainerName}
	cmd := exec.Command("docker", cmdArgs...)
	output, err := cmd.Output()
	if err != nil {
		fmt.Println(err.Error())
		return models.CreateResponse(false, err.Error())
	}
	var resp models.Response
	switch string(output) {
	case "true":
		resp = models.CreateResponse(true, "Container Running")
	case "false":
		resp = models.CreateResponse(false, "Container Stopped")
	}
	return resp
}

func (c *Container) GetFile(FilePath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "cat", FilePath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) CreateFile(FilePath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "sh", "-c", fmt.Sprintf("touch %s", FilePath))
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) UpdateFile(FilePath, FileContent string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "sh", "-c", fmt.Sprintf("echo %s >> %s", FileContent, FilePath))
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) DeleteFile(FilePath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "rm", FilePath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) GetFolderContents(FolderPath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "rm", FolderPath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) CreateFolder(FolderPath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "mkdir", FolderPath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) DeleteFolder(FolderPath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", c.ContainerName, "rm", "-rf", FolderPath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}
