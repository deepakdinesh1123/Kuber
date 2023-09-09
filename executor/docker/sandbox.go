package docker

import (
	"encoding/json"
	"executor/db"
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

func ExistingSandbox(SandboxID string) Sandbox {
	return Sandbox{
		SandboxID: SandboxID,
	}
}

func (s *Sandbox) CreateSandbox() (*Container, error) {
	if s.SandboxType == "compose" {
		// Support for compose will be added later
	} else {
		seed := time.Now().UTC().UnixNano()
		containerName := namegenerator.NewNameGenerator(seed).Generate()
		container := NewContainer(containerName, s.ImageName, s.SandboxConfig.ContConfig)
		out, err := container.CreateContainer()
		if err != nil {
			return nil, err
		}

		fmt.Println(out)

		return container, nil
	}
	return nil, nil
}

func (s *Sandbox) Delete() error {
	sandbox, err := db.GetSandboxByID(s.SandboxID)
	if err != nil {
		return err
	}
	type Containers struct {
		Containers []string `json:"containers"`
	}
	val, err := sandbox.Containers.GetJSON()
	var containers Containers
	if err := json.Unmarshal(val, &containers); err != nil {
		return err
	}
	err = db.DeleteSandboxByID(s.SandboxID)
	if err != nil {
		return err
	}
	container := ExistingContainer(containers.Containers[0])
	err = container.StopContainer()
	if err != nil {
		return err
	}
	err = container.DeleteContainer()
	if err != nil {
		return err
	}
	return nil
}
