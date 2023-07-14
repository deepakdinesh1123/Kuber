import axios from "axios";
import Cookies from "js-cookie";

export type JSON = {
  [key: string]: string | number | boolean | null | JSON | Array<string>;
};

export interface AxiosRequest {
  data: JSON;
  type: string;
  url: string;
  headers?: JSON;
}

export interface AxiosResponse {
  data: JSON;
  success: boolean;
}

export function handleApiRequest(request: AxiosRequest): AxiosResponse {
  if (request.headers != undefined) {
    request.headers = {
      Authorizaion: `Bearer ${Cookies.get("access_token")}`,
      ...request.headers,
    };
  }
  axios
    .request({
      url: request.url,
      baseURL: process.env.NEXT_PUBLIC_HOST,
      method: request.type,
      data: request.data,
    })
    .then((res) => {
      return res.data["response"], res.data["success"];
    })
    .catch((e) => {
      console.log(e);
    });
  return {
    data: {},
    success: false,
  };
}
