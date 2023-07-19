import React, { useEffect } from 'react';

const SignupWithGitHub: React.FC = () => {
  const handleSignup = () => {
    const clientId = 'c15c2a51e900aee7287c';
    const redirectUri = 'http://localhost:3000/redirect';

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
