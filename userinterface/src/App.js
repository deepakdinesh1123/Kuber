import React, { useState } from "react";
import { Resizable } from "react-resizable";
import BasicTree from "./FolderTree";
import Editor from "@monaco-editor/react";
import XtermComponent from "./XtermComponent";
import "./styles.css";

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
  const [recordedStream, setRecordedStream] = useState(null);
  const [isRecording, setIsRecording] = useState(false);

  const handleRecordClick = async () => {
    if (!isRecording) {
      try {
        const stream = await navigator.mediaDevices.getDisplayMedia({
          video: true,
        });
        const recorder = new MediaRecorder(stream);
        const recordedChunks = [];

        recorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            recordedChunks.push(event.data);
          }
        };

        recorder.onstop = () => {
          const recordedBlob = new Blob(recordedChunks, { type: "video/webm" });
          const url = URL.createObjectURL(recordedBlob);
          const a = document.createElement("a");
          a.style.display = "none";
          a.href = url;
          a.download = "screen-recording.webm";
          document.body.appendChild(a);
          a.click();
          URL.revokeObjectURL(url);

          if (stream.getVideoTracks().length > 0) {
            stream.getVideoTracks()[0].stop();
          }

          setIsRecording(false); // Update recording state after stopping
        };

        recorder.start();
        setRecordedStream(recorder);
        setIsRecording(true);
      } catch (error) {
        console.error("Error accessing screen media:", error);
      }
    } else {
      if (recordedStream) {
        recordedStream.stop();
      }
    }
  };

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
            <XtermComponent height={`${terminalHeight - 25}px`} />
          </div>
          <div className="RecordButtonContainer">
            <button
              className={`RecordButton ${isRecording ? "Recording" : ""}`}
              onClick={handleRecordClick}
            >
              {isRecording ? "Stop Recording" : "Start Recording"}
            </button>
          </div>
        </div>
      </Resizable>
    </div>
  );
}
