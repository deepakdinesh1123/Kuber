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
  const [jsonData, setJsonData] = useState(null); // State to store the JSON data

  const handleChange = (event) => {
    const { name, value } = event.target;
    setenvData((prevenvData) => ({
      ...prevenvData,
      [name]: value,
    }));
  };

  const handleConfigChange = (content: String) => {
    setConfig(content);
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

  const handleCodeChange = (content: string) => {
    setFileContent(content);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const jsonData = {
      name: envData.name,
      type: envData.type,
      image_name: envData.image_name,
      image_tag: envData.image_tag,
      config: config,
      docker_file_content: fileContent,
    };
    setJsonData(jsonData); // Store the JSON data in the state
    console.log(jsonData);
  };

  // ... (rest of the code)

  return (
    <>
      <form onSubmit={handleSubmit}>
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
          <select name="type" value={envData.type} onChange={handleChange}>
            <option value="default">Select Environment Type</option>
            <option value="docker">Docker</option>
            <option value="compose">Docker Compose</option>
          </select>
        </label>
        <br />
        <label>
          Image Name:
          <input
            name="image_name"
            value={envData.image_name}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Image Tag:
          <input
            name="image_tag"
            value={envData.image_tag}
            onChange={handleChange}
          />
        </label>

        <div style={{ display: "flex" }}>
          <input type="submit" value="Submit" />
        </div>
      </form>

      <div style={{ display: "flex" }}>
        <div style={{ flex: "6" }}>
          <MonacoEditor
            value={"#Enter your dockerfile"}
            onChange={handleCodeChange}
            language="dockerfile"
            width="100%"
            height="300px"
          />
        </div>
        <div style={{ flex: "3" }}>
          <MonacoEditor
            value={config}
            onChange={handleConfigChange}
            language="json"
            width="100%"
            height="300px"
          />
        </div>
      </div>
    </>
  );
}
