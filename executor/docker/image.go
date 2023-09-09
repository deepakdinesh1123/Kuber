package docker

import (
	"bytes"
	"fmt"
	"os/exec"
	"strings"
	"sync"
	"time"

	"executor/db"
	"executor/models"
)

func BuildImage(imageName, tag, dockerfile, userID string, ch chan models.Response, wg *sync.WaitGroup) {
	if exists, _ := CheckImageExists(fmt.Sprintf("%s-%s:%s", imageName, userID, tag)); !exists {
		imgNameWithId := fmt.Sprintf("%s-%s:%s", imageName, userID, tag)
		dockerFile := bytes.NewBufferString(dockerfile)

		cmd := exec.Command("docker", "build", "-t", imgNameWithId, "-")
		cmd.Stdin = dockerFile
		cmd.Stdout = nil

		err := cmd.Start()
		if err != nil {
			ch <- models.Response{Success: false, Message: err.Error()}
		}

		for {
			if exists, _ := CheckImageExists(imgNameWithId); exists {
				_ = cmd.Wait()
				break
			} else {
				ch <- models.Response{Message: "building"}
				time.Sleep(3 * time.Second)
			}
		}

		err = db.CreateNewImage(imgNameWithId, dockerfile, userID)
		if err != nil {
			ch <- models.Response{Success: false, Message: err.Error()}
		}
		ch <- models.Response{Message: imgNameWithId, Success: true}
	}
	ch <- models.Response{Success: false, Message: "Already exists"}
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
