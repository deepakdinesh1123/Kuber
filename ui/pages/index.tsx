import React, { useEffect } from "react";
import { getCookie } from "cookies-next";
import { useRouter } from "next/router";

const SignupWithGitHub: React.FC = () => {
  const router = useRouter();

  useEffect(() => {
    if (getCookie("access_token")) {
      router.push("/environments/dashboard");
    }
  });

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
