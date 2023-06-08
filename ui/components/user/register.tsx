import Cookies from "js-cookie";
import { useRouter } from "next/router";
import { useEffect, SyntheticEvent } from "react";

export default function Register() {

    const router = useRouter();

  const handleSubmit = (e: SyntheticEvent) => {
    e.preventDefault();
    const username = e.target[0].value;
    const email = e.target[1].value;
    const password = e.target[1].value;

    fetch(`${process.env.HOST}/account/api/register`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "username": username,
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
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
          />
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
}
