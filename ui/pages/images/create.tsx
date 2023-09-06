import Editor from "@monaco-editor/react";
import { useRef, useState } from "react";

export default function App() {
  const editorRef = useRef(null);
  const [imageName, setImageName] = useState("");
  const [tagName, setTagName] = useState("");

  function handleEditorDidMount(editor, monaco) {
    editorRef.current = editor;
  }

  function handleBuildClick() {
    const dockerfile = editorRef.current.getValue();

    if (!imageName.trim()) {
      alert("Image Name cannot be empty.");
    } else if (!dockerfile.trim()) {
      alert("Dockerfile cannot be empty.");
    } else if (!tagName.trim()) {
      const confirmed = window.confirm(
        "Tag is empty. Do you want to set it to 'latest'?",
      );
      if (confirmed) {
        setTagName("latest");
      }
    } else {
      const data = {
        ImageName: imageName,
        Dockerfile: dockerfile,
        Tag: tagName,
      };
      alert(`Building image: ${JSON.stringify(data)}`);
      console.log(data);
    }
  }

  return (
    <>
      <div>
        <label htmlFor="imageName">Image Name:</label>
        <input
          type="text"
          placeholder="Enter image name"
          value={imageName}
          onChange={(e) => setImageName(e.target.value)}
        />
        <label htmlFor="imageName">Tag:</label>
        <input
          type="text"
          placeholder="Enter tag"
          value={tagName}
          onChange={(e) => setTagName(e.target.value)}
        />
        <button onClick={handleBuildClick}>Build</button>
      </div>
      <Editor
        height="90vh"
        theme="vs-dark"
        defaultLanguage="dockerfile"
        defaultValue="# Enter your dockerfile here"
        onMount={handleEditorDidMount}
      />
    </>
  );
}
