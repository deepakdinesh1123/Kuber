import React, { useState, useEffect, SyntheticEvent } from "react";
import dynamic from "next/dynamic";

const MonacoEditor = dynamic(() => import("../../components/ide/editor"), {
  ssr: false,
});

export default function CreateEnvironment() {
  const [env, setEnv] = useState("");
  const [fileContent, setFileContent] = useState("");
  const [config, setConfig] = useState("Enter your config");

  const handleEnvChange = (event: SyntheticEvent) => {
    setEnv(event.target.value);
  };

  const handleConfigChange = (event: SyntheticEvent) => {
    setConfig(event.target.value);
  };

  const handleTextAreaKeyDown = (event: SyntheticEvent) => {
    if (event.keyCode === 9) {
      event.preventDefault();
      // TODO handle tab press properly
    }
  };

  const handleSubmit = () => {};

  const handleCodeChange = (content: string) => {
    setFileContent(content);
  };

  const [windowSize, setWindowSize] = useState({
    width: typeof window !== "undefined" ? window.innerWidth : 0,
    height: typeof window !== "undefined" ? window.innerHeight : 0,
  });

  useEffect(() => {
    function handleResize() {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }

    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <>
      <input
        type="text"
        placeholder="Enter the name of the environment"
        onChange={handleEnvChange}
      ></input>
      <button type="button" onClick={handleSubmit}>
        {" "}
        Submit
      </button>
      <div style={{ display: "flex" }}>
        <MonacoEditor
          value={"# Enter your dockerfile "}
          onChange={handleCodeChange}
          language="Docker"
          width="80%"
        />
        <textarea
          style={{
            backgroundColor: "black",
            caretColor: "white",
            width: "20%",
            height: "auto",
            color: "white",
          }}
          onKeyDown={handleTextAreaKeyDown}
          value={config}
          onChange={handleConfigChange}
        ></textarea>
      </div>
    </>
  );
}
