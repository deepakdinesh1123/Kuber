import { AxiosRequest, AxiosResponse, handleApiRequest } from "./api";

export async function handleCreateImage(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleGetUserImages(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleGetImageById(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}
