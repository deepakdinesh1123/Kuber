package docker

import (
	"fmt"

	"github.com/google/uuid"
)

type SandboxConfig struct {
	ContConfig ContainerConfig
	// additional fields will be added
}

type Sandbox struct {
	SandboxID       string
	SandboxName     string
	SandboxConfig   SandboxConfig
	SandboxType     string
	ProjectName     string
	ImageName       string
	EnvironmentName string
}

func NewSandboxConfig(contConfig ContainerConfig) SandboxConfig {
	return SandboxConfig{
		ContConfig: contConfig,
	}
}

func NewSandbox(sandboxName, sandboxType, projectName, environmentName, imageName string, config SandboxConfig) Sandbox {
	sandboxId := uuid.NewString()
	return Sandbox{
		SandboxID:       sandboxId,
		SandboxName:     sandboxName,
		SandboxConfig:   config,
		SandboxType:     sandboxType,
		ProjectName:     projectName,
		ImageName:       imageName,
		EnvironmentName: environmentName,
	}
}

func (s *Sandbox) CreateSandbox() (*Container, error) {
	if s.SandboxType == "compose" {
		// Support for compose will be added later
	} else {
		container := NewContainer(fmt.Sprintf("%s-%s-%s", s.EnvironmentName, s.SandboxName, s.SandboxID), s.ImageName, s.SandboxConfig.ContConfig)
		out, err := container.CreateContainer()
		if err != nil {
			return nil, err
		}
		fmt.Println(out)

		return container, nil
	}
	return nil, nil
}
