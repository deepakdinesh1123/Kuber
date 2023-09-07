import React, { useState } from "react";
import Editor from "@monaco-editor/react";
import styles from "../.././styles/CodeEditor.module.css";

const CodeEditor = ({
  selectedLanguage,
  editorContent,
  languageOptions,
  onLanguageChange,
  onContentChange,
  filename,
  onFilenameChange,
  appendExtension,
  onSaveFile,
}) => {
  return (
    <div className={styles["Monaco-editor"]}>
      <div>
        <select value={selectedLanguage} onChange={onLanguageChange}>
          {languageOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </div>
      <div className={styles["filename-input"]}>
        <input
          type="text"
          placeholder="Enter filename"
          value={filename}
          onChange={onFilenameChange}
        />
        <button onClick={appendExtension}>Save filename</button>
        <button onClick={onSaveFile}>Save file</button>
      </div>
      <div>
        <Editor
          height="70vh" // Adjust the height as needed
          language={selectedLanguage}
          theme="vs-dark"
          value={editorContent}
          onChange={onContentChange}
        />
      </div>
    </div>
  );
};

export default CodeEditor;
