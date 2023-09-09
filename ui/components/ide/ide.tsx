import React, { useState } from "react";
import CodeEditor from "./editor";
import XtermComponent from "./terminal";
import styles from "../../styles/ide.module.css";

const languageOptions = [
  { label: "JavaScript", value: "javascript" },
  { label: "Python", value: "python" },
  { label: "Java", value: "java" },
  { label: "C", value: "c" },
  { label: "C++", value: "cpp" },
  { label: "HTML", value: "html" },
];

function IDE() {
  const [editorContent, setEditorContent] = useState({
    javascript: "",
    python: "",
    java: "",
    c: "",
    cpp: "",
    html: "",
  });

  const [selectedLanguage, setSelectedLanguage] = useState("javascript");
  const [filename, setFilename] = useState("");

  const handleLanguageChange = (
    event: React.ChangeEvent<HTMLSelectElement>,
  ) => {
    setSelectedLanguage(event.target.value);
  };

  const handleFilenameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFilename(event.target.value);
  };

  const appendExtension = () => {
    const currentLanguage = selectedLanguage;
    const ext = {
      javascript: ".js",
      python: ".py",
      java: ".java",
      c: ".c",
      cpp: ".cpp",
      html: ".html",
    }[currentLanguage];

    if (filename && !filename.endsWith(ext)) {
      setFilename(filename + ext);
    }
  };

  const handleSaveFile = () => {
    if (filename == "") {
      alert("Filename cannot be empty");
      return;
    }
    const requestData = {
      filename,
      editorContent: editorContent[selectedLanguage],
    };

    const requestBody = JSON.stringify(requestData);
    console.log(requestBody);
  };

  return (
    <div className={styles["ide-container"]}>
      <div className={styles["editor-section"]}>
        <CodeEditor
          selectedLanguage={selectedLanguage}
          editorContent={editorContent[selectedLanguage]}
          languageOptions={languageOptions}
          onLanguageChange={handleLanguageChange}
          onContentChange={(newValue: string) =>
            setEditorContent({
              ...editorContent,
              [selectedLanguage]: newValue,
            })
          }
          filename={filename}
          onFilenameChange={handleFilenameChange}
          appendExtension={appendExtension}
          onSaveFile={handleSaveFile}
        />
      </div>
      <div className={styles["terminal-section"]}>
        <h4>Terminal</h4>
        <div className={styles["terminal-container"]}>
          <XtermComponent />
        </div>
      </div>
    </div>
  );
}

export default IDE;
