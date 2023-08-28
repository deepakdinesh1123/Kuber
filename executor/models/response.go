package models

type Response struct {
	success bool
	message string
}

func CreateResponse(success bool, message string) Response {
	return Response{
		success: success,
		message: message,
	}
}
