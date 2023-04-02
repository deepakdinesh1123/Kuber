package execution

import (
	context "context"
	"os/exec"

	"github.com/docker/docker/client"
)

type Server struct {
	UnimplementedExecuteServer
	DockerClient *client.Client
}

func (s *Server) ExecuteCommand(ctx context.Context, in *ExecuteRequest) (*ExecutionResponse, error) {
	res, err := exec.Command("bash", "-c", in.Command).Output()
	if err != nil {
		return &ExecutionResponse{
			Responses: &ExecutionResponse_Error{
				Error: &Error{
					Error: err.Error(),
				},
			},
		}, nil
	}
	return &ExecutionResponse{
		Responses: &ExecutionResponse_Success{
			Success: &ExecutionSuccess{
				Result: string(res),
			},
		},
	}, nil
}
