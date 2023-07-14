import React, {
  FormEventHandler,
  SyntheticEvent,
  useEffect,
  useState,
} from "react";
import { useRouter } from "next/router";
import Cookies from "js-cookie";

export default function Login() {
  const router = useRouter();

  const handleSubmit = (e: SyntheticEvent) => {
    e.preventDefault();
    const email = e.target[0].value;
    const password = e.target[1].value;
    const formdata = new FormData();
    formdata.append("password", password);
    formdata.append("email", email);

    const requestOptions: RequestInit = {
      method: "POST",
      headers: new Headers(),
      body: formdata,
      redirect: "follow",
    };

    fetch(`${process.env.NEXT_PUBLIC_HOST}/api/login/`, requestOptions)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((result) => {
        console.log(result);
        Cookies.set("logged_in", "true");
        Cookies.set("access_token", result["access"]);
        router.push("http://localhost:3000/environments/list");
      })
      .catch((error) => console.log("error", error));
  };

  useEffect(() => {});

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email:</label>
      <input type="email" id="email" />
      <label htmlFor="password">Password:</label>
      <input type="password" id="password" />
      <button type="submit">Log In</button>
    </form>
  );
}
