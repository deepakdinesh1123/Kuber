import { AxiosRequest, AxiosResponse, handleApiRequest } from "./api";

export async function handleCreateEnvironment(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function getMachine(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleGetEnvironment(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleCreateSandbox(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}
