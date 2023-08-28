import Editor from "@monaco-editor/react";
import { useRef } from "react";

export default function App() {
  const editorRef = useRef(null);

  function handleEditorDidMount(editor, monaco) {
    editorRef.current = editor;
  }

  function showValue() {
    alert(editorRef.current.getValue());
  }

  return (
    <>
      <button onClick={showValue}>Show value</button>
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
