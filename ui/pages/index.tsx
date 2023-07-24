import React, { useEffect } from "react";

const SignupWithGitHub: React.FC = () => {
  const handleSignup = () => {
    const clientId = process.env.GITHUB_CLIENT_ID;
    const redirectUri = process.env.GIT_REDIRECT_URL;

    // Redirect the user to GitHub's authorization endpoint
    window.location.href = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}`;
  };

  return (
    <div>
      <h1>Signup with GitHub</h1>
      <button onClick={handleSignup}>Sign up with GitHub</button>
    </div>
  );
};

export default SignupWithGitHub;
