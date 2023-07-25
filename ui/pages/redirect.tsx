import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import Cookies from "js-cookie";
import { handleGithubAuthRequest } from "@/utils/service/ui";
import { setCookie } from "cookies-next";

const RedirectPage = () => {
  const router = useRouter();
  const [code, setCode] = useState<string | null>(null);
  const [requestStatus, setRequestStatus] = useState<string>("");
  const [accessToken, setAccessToken] = useState<string>("");

  useEffect(() => {
    const { query } = router;
    const code = query.code;

    if (code) {
      setCode(code as string);
      sendPostRequest(code as string);
    }
  }, [router]);

  useEffect(() => {
    const accessToken = Cookies.get("access_token");
    setAccessToken(accessToken || "");
  }, []);

  const sendPostRequest = async (code: string) => {
    try {
      const request = {
        data: {
          code: code,
        },
        type: "post",
        url: "/users/auth/github/",
      };
      const response = await handleGithubAuthRequest(request);
      const jwt_token = response.data;
      setCookie("access_token", jwt_token);
    } catch (error) {
      console.error("Error:", error);
      setRequestStatus("Error: " + error);
    }
  };

  return (
    <div>
      {code ? <p>Code: {code}</p> : <div>Loading...</div>}
      {requestStatus && <p>{requestStatus}</p>}
      <p>Access Token: {accessToken}</p>
    </div>
  );
};

export default RedirectPage;
