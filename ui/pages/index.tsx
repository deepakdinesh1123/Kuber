import React, { useEffect, useState } from "react";
import { getCookie } from "cookies-next";
import { useRouter } from "next/router";
import { handleGithubAuthRequest } from "@/utils/service/ui";
import { setCookie } from "cookies-next";

const SignupWithGitHub: React.FC = () => {
  const router = useRouter();
  const [code, setCode] = useState<string | null>(null);

  useEffect(() => {
    if (getCookie("access_token")) {
      router.push("/dashboard");
      console.log(getCookie("access_token"));
    }
  });

  useEffect(() => {
    const { query } = router;
    const code = query.code;

    if (code) {
      setCode(code as string);
      sendPostRequest(code as string);
    }
  }, [router]);

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
      router.push("/dashboard");
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleSignup = () => {
    const clientId = process.env.NEXT_PUBLIC_GITHUB_CLIENT_ID;
    const redirectUri = process.env.NEXT_PUBLIC_GIT_REDIRECT_URL;
    // Redirect the user to GitHub's authorization endpoint
    window.location.href = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&scope=user:email`;
  };

  return (
    <div>
      <h1>Signup with GitHub</h1>
      <button onClick={handleSignup}>Sign up with GitHub</button>
    </div>
  );
};

export default SignupWithGitHub;
