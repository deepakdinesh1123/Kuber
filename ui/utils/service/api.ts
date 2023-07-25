import axios from "axios";
import { getCookie } from "cookies-next";

export type JSON = Record<
  string,
  string | number | boolean | null | JSON | Array<string>
>;

export interface AxiosRequest {
  data?: JSON;
  type: string;
  url: string;
  baseUrl: string;
  headers?: JSON;
}

export interface AxiosResponse {
  data: JSON;
  success: boolean;
}

export async function handleApiRequest(
  request: AxiosRequest,
): Promise<AxiosResponse> {
  if (getCookie("access_token")) {
    request.headers = {
      Authorization: `Bearer ${getCookie("access_token")}`,
      ...request.headers,
    };
  }

  try {
    const response = await axios.request({
      url: request.url,
      baseURL: "http://localhost:8000",
      method: request.type,
      data: request.data,
      headers: request.headers,
    });

    return {
      data: response.data.data,
      success: response.data.success,
    };
  } catch (error) {
    console.log(error);
    return {
      data: {},
      success: false,
    };
  }
}
