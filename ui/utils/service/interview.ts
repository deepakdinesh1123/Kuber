import { AxiosRequest, AxiosResponse, handleApiRequest } from "./api";

export async function handleCreateInterview(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleGetInterview(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleGetForm(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}
