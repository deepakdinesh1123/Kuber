import Login from "@/components/user/login";
import Register from "@/components/user/register";
import { useState } from "react";

export default function Index() {

  const [showRegister, setShowRegister] = useState(false);
  return <>
    {!showRegister ?
        <div>
        <Login /> <div onClick={() => setShowRegister(true)}>Register</div>
        </div>
        :
        <div>
        <Register/> <div onClick={() => setShowRegister(false)}>Login</div>
      </div>}
  </>
}
