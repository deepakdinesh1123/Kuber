package docker

import (
	"bytes"
	"fmt"
	"os/exec"
	"strings"

	"github.com/google/uuid"
)

func BuildImage(imageName, tag, dockerfile string) (string, string, error) {
	if exists, _ := CheckImageExists(imageName); !exists {
		imgNameWithId := fmt.Sprintf("%s-%s:%s", imageName, uuid.NewString(), tag)
		dockerFile := bytes.NewBufferString(dockerfile)

		cmd := exec.Command("docker", "build", "-t", imgNameWithId, "-")
		cmd.Stdin = dockerFile
		cmd.Stdout = nil

		out, err := cmd.Output()
		if err != nil {
			return "", "", err
		}

		return string(out), imgNameWithId, nil
	}
	return "exists", imageName, nil
}

func CheckImageExists(imageName string) (bool, error) {
	cmd := exec.Command("docker", "image", "inspect", imageName, "--format=xizt")
	out, err := cmd.Output()
	if err != nil {
		// Handle the error appropriately, for example:
		if exitErr, ok := err.(*exec.ExitError); ok {
			// The command exited with a non-zero status
			fmt.Println("Error:", exitErr)
			return false, nil // or return false, exitErr if you want to return the error
		}
		return false, err
	}
	outStr := strings.TrimSpace(string(out))
	if outStr == "xizt" {
		return true, nil
	}
	return false, nil
}
