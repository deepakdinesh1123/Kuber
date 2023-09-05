package models

type Response struct {
	Success bool   `json:"Success"`
	Message string `json:"Message"`
}

func CreateResponse(success bool, message string) Response {
	return Response{
		Success: success,
		Message: message,
	}
}
