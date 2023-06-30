import { AxiosRequest, AxiosResponse, handleApiRequest } from './api';


export function handleCreateEnvironment(request: AxiosRequest): AxiosResponse {
    return handleApiRequest(request);
}

export function getMachine(request: AxiosRequest): AxiosResponse {
    return handleApiRequest(request);
}
