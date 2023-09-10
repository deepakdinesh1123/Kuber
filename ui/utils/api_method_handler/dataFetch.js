// dataFetching.js

import { handleGetEnvironment } from "@/utils/service/environment";
import { handleGetInterview } from "@/utils/service/interview";
import { handleGetSandbox } from "@/utils/service/sandbox";

export const fetchEnvironmentData = async () => {
  const request = {
    type: "GET",
    url: "/environments/environment",
  };
  return await handleGetEnvironment(request);
};

export const fetchInterviewData = async () => {
  const request = {
    type: "GET",
    url: "/interviews/interview",
  };
  return await handleGetInterview(request);
};

export const fetchSandboxData = async () => {
  const request = {
    type: "GET",
    url: "/environments/sandbox",
  };
  return await handleGetSandbox(request);
};
