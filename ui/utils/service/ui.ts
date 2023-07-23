import { AxiosRequestConfig, AxiosResponse } from 'axios';
import axios from 'axios';
import dotenv from 'dotenv';

export function handleGithubAuthRequest(code: string): Promise<AxiosResponse> {
  dotenv.config()
  const requestConfig: AxiosRequestConfig = {
    method: 'POST',
    url: process.env.GIT_AUTH_URL,
    headers: {
      'Content-Type': 'application/json',
    },
    data: {
      code,
    },
  };

  return axios(requestConfig);
}
