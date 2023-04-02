package server

import (
	"google.golang.org/grpc"
)

func NewServer() (*grpc.Server, error) {
	s := grpc.NewServer()
	return s, nil
}
