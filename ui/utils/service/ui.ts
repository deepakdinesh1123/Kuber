import { AxiosRequest, AxiosResponse, handleApiRequest } from "./api";

export async function handleGithubAuthRequest(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  return await handleApiRequest(request);
}
