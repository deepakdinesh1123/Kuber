import React, { FormEventHandler, SyntheticEvent, useEffect, useState } from "react";
import { useRouter } from "next/router";
import Cookies from "js-cookie";

export default function Login() {
  const router = useRouter();

  const handleSubmit = (e: SyntheticEvent) => {
    e.preventDefault();
    const email = e.target[0].value;
    const password = e.target[1].value;

    fetch('http://localhost:8000/account/api/login', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "email": email,
        "password": password
      })
    }).then( res => {
      if(res.status == 405) {
        console.log("User already exists");
      }
      else {
        Cookies.set('logged_in', 'true');
        router.push("http://localhost:3000/environment")
      }
    });
  };

  useEffect( () => {

  });

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email:</label>
      <input
        type="email"
        id="email"
      />
      <label htmlFor="password">Password:</label>
      <input
        type="password"
        id="password"
      />
      <button type="submit">Log In</button>
    </form>
  );
};
