import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Cookies from 'js-cookie';

const RedirectPage = () => {
  const router = useRouter();
  const [code, setCode] = useState<string | null>(null);
  const [requestStatus, setRequestStatus] = useState<string>('');
  const [accessToken, setAccessToken] = useState<string>('');

  useEffect(() => {
    const { query } = router;
    const code = query.code;

    if (code) {
      setCode(code as string);
      sendPostRequest(code as string);
    }
  }, [router]);

  useEffect(() => {
    const accessToken = Cookies.get('access_token');
    setAccessToken(accessToken || '');
  }, []);

  const sendPostRequest = async (code: string) => {
    try {
      const response = await fetch('http://localhost:8000/users/auth/github', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      });

      if (response.ok) {
        setRequestStatus('POST request sent successfully');
      } else {
        setRequestStatus('Failed to send POST request');
      }
    } catch (error) {
      console.error('Error:', error);
      setRequestStatus('Error: ' + error);
    }
  };

  return (
    <div>
      {code ? (
        <p>Code: {code}</p>
      ) : (
        <div>Loading...</div>
      )}
      {requestStatus && <p>{requestStatus}</p>}
      <p>Access Token: {accessToken}</p>
    </div>
  );
};

export default RedirectPage;
