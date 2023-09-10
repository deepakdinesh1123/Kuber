import { AxiosRequest, AxiosResponse, handleApiRequest } from "./api";

export async function handleGetSandbox(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}

export async function handleDelSandbox(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}
