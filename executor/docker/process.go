package docker

import (
	"bufio"
	"context"
	"errors"
	"io"
	"os/exec"
	"strings"
	"sync"
	"time"
)

type Process struct {
	ContainerName string
	Command       []string
	Dir           string
	Proc          *exec.Cmd
	Pid           string
	Lock          sync.Mutex
	stdin         io.WriteCloser
	stdout        io.Reader
}

func NewProcess(containerName string, command []string, dir string) *Process {
	return &Process{
		ContainerName: containerName,
		Command:       command,
		Dir:           dir,
	}
}

func (p *Process) Start() error {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	cmdPrefix := []string{"exec", "-i", p.ContainerName}
	cmd := append(cmdPrefix, p.Command...)
	p.Proc = exec.Command("docker", cmd...)
	p.Proc.Dir = p.Dir

	var err error
	p.stdin, err = p.Proc.StdinPipe()
	if err != nil {
		return err
	}
	p.stdout, err = p.Proc.StdoutPipe()
	if err != nil {
		return err
	}

	return p.Proc.Start()
}

func (p *Process) GetPID() (string, error) {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	cmd := exec.Command("docker", "exec", "-i", p.ContainerName, "pgrep", "-a", ".")
	output, err := cmd.Output()
	if err != nil {
		return "", err
	}

	lines := strings.Split(strings.TrimSpace(string(output)), "\n")
	for _, line := range lines {
		parts := strings.Fields(line)
		if len(parts) >= 2 {
			pid := parts[0]
			cmd := strings.Join(parts[1:], " ")
			if cmd == strings.Join(p.Command, " ") {
				p.Pid = pid
				return pid, nil
			}
		}
	}

	return "", nil
}

func (p *Process) IsAlive() bool {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	if p.Pid == "" {
		return false
	}

	cmd := exec.Command("docker", "exec", "-i", p.ContainerName, "ps", "-p", p.Pid)
	err := cmd.Run()
	return err == nil
}

func (p *Process) ReadLine() (string, error) {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	reader := bufio.NewReader(p.stdout)
	line, _, err := reader.ReadLine()
	return string(line), err
}

func (p *Process) ReadLineWithTimeout(timeout time.Duration) (string, error) {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()

	reader := bufio.NewReader(p.stdout)
	var line string
	var err error

	go func() {
		select {
		case <-ctx.Done():
			err = errors.New("Timeout")
		default:
			var lineBytes []byte
			lineBytes, _, err = reader.ReadLine()
			line = string(lineBytes)
		}
	}()

	<-ctx.Done()
	return line, err
}

func (p *Process) ReadOutput() (string, error) {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	output, err := io.ReadAll(p.stdout)
	if err != nil {
		return "", err
	}

	return string(output), nil
}

func (p *Process) Kill() error {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	if p.Proc.Process != nil {
		return p.Proc.Process.Kill()
	}
	return nil
}

func (p *Process) WriteInput(input string) error {
	p.Lock.Lock()
	defer p.Lock.Unlock()

	_, err := io.WriteString(p.stdin, input+"\n")
	if err != nil {
		return err
	}
	return nil
}
