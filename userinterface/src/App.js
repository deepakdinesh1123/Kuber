import React, { useEffect, useRef, useState } from "react";
import { Resizable } from "react-resizable";
import BasicTree from "./FolderTree";
import Editor from "@monaco-editor/react";
import XtermComponent from "./XtermComponent";
import "./styles.css";
import Cookies from "js-cookie";

const languageOptions = [
  { label: "JavaScript", value: "javascript" },
  { label: "Python", value: "python" },
  { label: "Java", value: "java" },
  { label: "C", value: "c" },
  { label: "C++", value: "cpp" },
  { label: "HTML", value: "html" },
  // Add more programming languages as needed
];

export default function App() {
  useEffect(() => {
    if (Cookies.get("access_token") === undefined) {
      window.location.href = "http://localhost:3000";
    }
  });

  const [editorContent, setEditorContent] = useState({
    javascript: "",
    python: "",
    java: "",
    c: "",
    cpp: "",
    html: "",
    // Add more language keys with empty strings for other languages
  });

  const [selectedLanguage, setSelectedLanguage] = useState("javascript");
  const [terminalHeight, setTerminalHeight] = useState(150); // Initial height of the terminal
  const [container, setContainer] = useState("nerdy-fuchsia-spider");
  const workdir = useRef("/");

  const handleLanguageChange = (event) => {
    const currentLanguage = selectedLanguage;
    const currentEditorContent = editorContent[currentLanguage];
    setEditorContent({
      ...editorContent,
      [currentLanguage]: currentEditorContent,
    });

    setSelectedLanguage(event.target.value);
  };

  const handleResize = (event, { size }) => {
    setTerminalHeight(size.height);
  };

  return (
    <div className="App">
      <div className="Sidebar FileManager">
        <BasicTree />
      </div>
      <Resizable
        height={terminalHeight}
        onResize={handleResize}
        minHeight={100}
        maxHeight={400}
        handle={<div className="ResizableHandle" />}
        axis="y"
      >
        <div className="EditorTerminalContainer">
          <div className="MonacoEditor">
            <div>
              <select value={selectedLanguage} onChange={handleLanguageChange}>
                {languageOptions.map((option) => (
                  <option key={option.value} value={option.value}>
                    {option.label}
                  </option>
                ))}
              </select>
            </div>
            <Editor
              height="90vh"
              language={selectedLanguage}
              theme="vs-dark"
              value={editorContent[selectedLanguage]}
              onChange={(newValue) =>
                setEditorContent({
                  ...editorContent,
                  [selectedLanguage]: newValue,
                })
              }
            />
          </div>
          <div className="Terminal">
            <h1>Terminal</h1>
            <XtermComponent
              height={`${terminalHeight - 25}px`}
              container={container}
              workdir={workdir}
            />
          </div>
        </div>
      </Resizable>
    </div>
  );
}
