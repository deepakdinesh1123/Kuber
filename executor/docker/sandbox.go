package docker

import (
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/goombaio/namegenerator"
)

type SandboxConfig struct {
	ContConfig ContainerConfig
	// additional fields will be added
}

type Sandbox struct {
	SandboxID     string
	SandboxName   string
	SandboxConfig SandboxConfig
	SandboxType   string
	ProjectName   string
	ImageName     string
	environmentID string
}

func NewSandboxConfig(contConfig ContainerConfig) SandboxConfig {
	return SandboxConfig{
		ContConfig: contConfig,
	}
}

func NewSandbox(sandboxName, sandboxType, projectName, environmentID, imageName string, config SandboxConfig) Sandbox {
	sandboxId := uuid.NewString()
	return Sandbox{
		SandboxID:     sandboxId,
		SandboxName:   sandboxName,
		SandboxConfig: config,
		SandboxType:   sandboxType,
		ProjectName:   projectName,
		ImageName:     imageName,
		environmentID: environmentID,
	}
}

func (s *Sandbox) CreateSandbox() (*Container, error) {
	if s.SandboxType == "compose" {
		// Support for compose will be added later
	} else {
		seed := time.Now().UTC().UnixNano()
		containerName := namegenerator.NewNameGenerator(seed).Generate()
		container := NewContainer(fmt.Sprintf(containerName, s.environmentID, s.SandboxName, s.SandboxID), s.ImageName, s.SandboxConfig.ContConfig)
		out, err := container.CreateContainer()
		if err != nil {
			return nil, err
		}

		fmt.Println(out)

		return container, nil
	}
	return nil, nil
}
