import axios from "axios";
import Cookies from "js-cookie";


export type JSON = {
    [key: string]: string | number | boolean | null | JSON | Array<string>;
  };

  export interface AxiosRequest {
    data?: JSON,
    type: string,
    url: string,
    headers?: JSON
  };

  export interface AxiosResponse {
    data: JSON,
    success: boolean
  };


export async function handleApiRequest(request: AxiosRequest): Promise<AxiosResponse> {
    // if (request.headers != undefined) {
    //     request.headers = {
    //         "Authorizaion": `Bearer ${Cookies.get("access_token")}`,
    //         ...request.headers
    //     }
    // }
    try {
        const response = await axios.request({
          url: request.url,
          baseURL: process.env.NEXT_PUBLIC_HOST,
          method: request.type,
          data: request.data,
        });
        return {
          data: response.data.response,
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
