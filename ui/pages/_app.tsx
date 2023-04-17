import type { AppProps } from 'next/app';
import App from 'next/app';
import { useRouter } from 'next/router';
import { useEffect } from 'react';
import Cookies from 'js-cookie';

export default function QuberApp({ Component, pageProps }: AppProps) {
  const router = useRouter();

  useEffect(() => {
    const loggedIn = pageProps.LoggedIn || false;
    if(!loggedIn && router.pathname !== "/") {
      router.push("/");
    }
  }, [pageProps]);
  return <Component {...pageProps} />
}

QuberApp.getInitialProps = async (appContext) => {
  const appProps = await App.getInitialProps(appContext);
  const loggedIn = Cookies.get('logged_in');
  return { ...appProps, pageProps: {loggedIn}};
}
