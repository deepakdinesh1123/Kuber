package docker

// import (
// 	"bufio"
// 	"context"
// 	"errors"
// 	"io"
// 	"os/exec"
// 	"time"
// )

// func ReadLineWithTimeout(timeout time.Duration, stdout io.Reader) (string, error) {
// 	ctx, cancel := context.WithTimeout(context.Background(), timeout)
// 	defer cancel()

// 	reader := bufio.NewReader(p.stdout)
// 	var line string
// 	var err error

// 	go func() {
// 		select {
// 		case <-ctx.Done():
// 			err = errors.New("Timeout")
// 		default:
// 			var lineBytes []byte
// 			lineBytes, _, err = reader.ReadLine()
// 			line = string(lineBytes)
// 		}
// 	}()

// 	<-ctx.Done()
// 	return line, err
// }

// func GetLogs(containerName string, containerLogs chan string) (string, error) {

// 	cmd := exec.Command("docker", "logs", containerName)
// 	stdout, err := cmd.StdoutPipe()
// 	if err != nil {
// 		return "", err
// 	}
// 	cmd.Stdin = nil

// 	for {

// 	}

// 	return "done", nil
// }
