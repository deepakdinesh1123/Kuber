package docker

import (
	"bytes"
	"fmt"
	"os/exec"
	"strings"

	"executor/db"

	"github.com/rs/zerolog/log"
)

func BuildImage(imageName, tag, dockerfile, userID string) (string, string, error) {
	if exists, _ := CheckImageExists(fmt.Sprintf("%s-%s:%s", imageName, userID, tag)); !exists {
		imgNameWithId := fmt.Sprintf("%s-%s:%s", imageName, userID, tag)
		dockerFile := bytes.NewBufferString(dockerfile)

		cmd := exec.Command("docker", "build", "-t", imgNameWithId, "-")
		cmd.Stdin = dockerFile
		cmd.Stdout = nil

		out, err := cmd.Output()
		if err != nil {
			return "", "", err
		}

		log.Debug().Str("Image", "ct")
		_, err = db.CreateNewImage(imgNameWithId, dockerfile, userID)
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

func DeleteImage(imageName string) (bool, error) {
	cmd := exec.Command("docker", "rmi", imageName)
	_, err := cmd.Output()
	if err != nil {
		// Handle the error appropriately, for example:
		if exitErr, ok := err.(*exec.ExitError); ok {
			// The command exited with a non-zero status
			fmt.Println("Error:", exitErr)
			return false, nil // or return false, exitErr if you want to return the error
		}
		return false, err
	}
	return true, nil
}
