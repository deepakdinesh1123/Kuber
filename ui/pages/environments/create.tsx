import React, { useState, useEffect, SyntheticEvent } from "react";
import dynamic from "next/dynamic";
import {
  handleCreateEnvironment,
  getMachine,
} from "@/utils/service/environment";

const MonacoEditor = dynamic(() => import("../../components/ide/editor"), {
  ssr: false,
});

export default function CreateEnvironment() {
  const [envData, setenvData] = useState({
    name: "",
    type: "",
    image_name: "",
    image_tag: "",
  });
  const [fileContent, setFileContent] = useState("");
  const [config, setConfig] = useState("Enter your config");
  const [configureEnv, setConfigureEnv] = useState(true);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setenvData((prevenvData) => ({
      ...prevenvData,
      [name]: value,
    }));
  };

  const handleConfigChange = (event: SyntheticEvent) => {
    setConfig(event.target.value);
  };

  const handleTextAreaKeyDown = (event: SyntheticEvent) => {
    if (event.keyCode === 9) {
      event.preventDefault();
      const { selectionStart, selectionEnd, value } = event.target;
      const newValue =
        value.substring(0, selectionStart) +
        "    " + // Four spaces
        value.substring(selectionEnd);

      // Update the textarea value and set the new cursor position
      event.target.value = newValue;
      setConfig(newValue);
      event.target.setSelectionRange(selectionStart + 4, selectionStart + 4);
    }
  };

  const EnvDetailsForm = () => {
    return (
      <form>
        <label>
          Environment Name:
          <input
            type="text"
            name="name"
            value={envData.name}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Environment Type:
          <select onChange={handleChange}>
            <option value="default">Select Environemnt Type</option>
            <option value="docker">Docker</option>
            <option value="compose">Docker Compose</option>
          </select>
        </label>
        <br />
        <label>
          Image Name:
          <input
            name="message"
            value={envData.image_name}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Image Tag:
          <input
            name="message"
            value={envData.image_tag}
            onChange={handleChange}
          />
        </label>
        <br />
        <button
          onClick={() => {
            setConfigureEnv(false);
          }}
        >
          Configure Docker
        </button>
      </form>
    );
  };
  const handleCodeChange = (content: string) => {
    setFileContent(content);
  };

  const handleSubmit = (event) => {
    const request = {
      data: {
        name: envData.name,
        config: config,
        images: [`${envData.image_name}`],
        type: envData.type,
      },
      type: "POST",
      url: "/environment/api/v1/createEnvironment/",
    };
    const resp = handleCreateEnvironment(request);
    console.log(resp);
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
      {configureEnv ? (
        <EnvDetailsForm />
      ) : (
        <div>
          <div style={{ display: "flex" }}>
            <button type="button" onClick={handleSubmit}>
              Submit
            </button>
            <button
              type="button"
              onClick={() => {
                setConfigureEnv(true);
              }}
            >
              Configgure Environment
            </button>
          </div>

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
        </div>
      )}
    </>
  );
}
