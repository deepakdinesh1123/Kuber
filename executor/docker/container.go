package docker

import (
	"fmt"
	"os/exec"

	"executor/models"
)

type ContainerConfig struct {
	port    *int
	volumes *[]string
}

type Container struct {
	ContainerName string
	ImageName     string
	ID            *string
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
		ID:            nil,
		Config:        &Config,
	}
}

func ExistingContainer(ContainerName string) *Container {
	return &Container{
		ContainerName: ContainerName,
		ImageName:     "",
		ID:            nil,
		Config:        nil,
	}
}

func (c *Container) CreateContainer() (string, error) {
	cmdArgs := []string{"run", "--name=" + c.ContainerName, "-d", "-t"}
	cmdArgs = append(cmdArgs, c.ImageName)

	cmd := exec.Command("docker", cmdArgs...)
	cmd.Stdout = nil
	cmd.Stderr = nil
	if err := cmd.Run(); err != nil {
		fmt.Println("Error creating container:", err)
		return "", err
	}
	return "Container created", nil
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
	cmd := exec.Command("docker", "exec", "-i", "cat", FilePath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) CreateFile(FilePath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", "touch", FilePath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) UpdateFile(FilePath, FileContent string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", "sh", "-c", fmt.Sprintf("echo %s >> %s", FileContent, FileContent))
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) DeleteFile(FilePath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", "rm", FilePath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) GetFolderContents(FolderPath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", "rm", FolderPath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) CreateFolder(FolderPath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", "mkdir", FolderPath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}

func (c *Container) DeleteFolder(FolderPath string) (string, error) {
	cmd := exec.Command("docker", "exec", "-i", "rm", "-rf", FolderPath)
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(output), nil
}
