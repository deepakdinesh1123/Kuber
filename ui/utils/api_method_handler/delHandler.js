import { handleDelEnvironment } from "@/utils/service/environment";
import { handleDelInterview } from "@/utils/service/interview";
import { handleDelSandbox } from "@/utils/service/sandbox";

export const delEnvironment = async (environmentId) => {
  const request = {
    type: "DELETE",
    url: `/environments/environment/${environmentId}`,
  };
  return await handleDelEnvironment(request);
};

export const delInterview = async (interviewId) => {
  const request = {
    type: "DELETE",
    url: `/interviews/interview/${interviewId}`,
  };
  return await handleDelInterview(request);
};

export const delSandbox = async (sandboxId) => {
  const request = {
    type: "DELETE",
    url: `/environments/sandbox/${sandboxId}`,
  };
  return await handleDelSandbox(request);
};
