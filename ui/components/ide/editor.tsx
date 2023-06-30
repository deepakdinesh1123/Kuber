import { useRef, useEffect, useState } from 'react';
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api';
import 'monaco-editor/esm/vs/basic-languages/python/python.contribution';
import 'monaco-editor/esm/vs/editor/editor.all.js';
import { registerfileLanguage } from '../../utils/lang_support/lang_reg.js'

type MonacoEditorProps = {
  value: string;
  onChange: (newValue: string) => void;
  language: string;
  width?: string;
  height?: string;
};


const MonacoEditor = ({ value, onChange, language, width, height }: MonacoEditorProps) => {
  const [screenSize, getDimension] = useState({
    dynamicWidth: window.innerWidth,
    dynamicHeight: window.innerHeight
  });
  const setDimension = () => {
    getDimension({
      dynamicWidth: window.innerWidth,
      dynamicHeight: window.innerHeight
    })
  }
  const editorRef = useRef<monaco.editor.IStandaloneCodeEditor | null>(
    null
  );

  useEffect(() => {
    registerfileLanguage();
    // initialize the Monaco editor
    editorRef.current = monaco.editor.create(
      document.getElementById('monaco-editor')!,
      {
        theme: 'vs-dark',
        language: language,
        value: value

      }
    );
    monaco.editor.setTheme('vs-dark');

    // listen for changes
    editorRef.current.onDidChangeModelContent(() => {
      onChange(editorRef.current!.getValue());
    });
    window.addEventListener('resize', setDimension);


    // cleanup function
    return () => {
      editorRef.current!.dispose();
      window.removeEventListener('resize', setDimension);
    };
  }, [screenSize]);

  return (
    <div
      id="monaco-editor"
      style={{ height: height || screenSize.dynamicHeight, width: width || screenSize.dynamicWidth }}
    ></div>

  );
};

export default MonacoEditor;
