import { useRef, useEffect, useState } from 'react';
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api';
import 'monaco-editor/esm/vs/basic-languages/python/python.contribution';
import 'monaco-editor/esm/vs/editor/editor.all.js';
import { registerfileLanguage } from '../../utils/lang_support/lang_reg.js';

type MonacoEditorProps = {
  value: string;
  onChange: (newValue: string) => void;
  language: string;
  width?: string;
  height?: string;
};

const MonacoEditor = ({ value, onChange, language, width, height }: MonacoEditorProps) => {
  const [screenSize, setScreenSize] = useState({
    dynamicWidth: window.innerWidth,
    dynamicHeight: window.innerHeight
  });
  const editorRef = useRef<monaco.editor.IStandaloneCodeEditor | null>(null);
  const modelRef = useRef<monaco.editor.ITextModel | null>(null);

  useEffect(() => {
    registerfileLanguage();

    // Initialize the Monaco editor
    editorRef.current = monaco.editor.create(
      document.getElementById('monaco-editor')!,
      {
        theme: 'vs-dark',
        language: 'rust',
        value: value
      }
    );
    monaco.editor.setTheme('vs-dark');

    // Set the model
    modelRef.current = editorRef.current.getModel();

    // Enable code completion
    monaco.languages.register({
      id: language
    });

    // Load the language's contribution
    monaco.languages.onLanguage(language, () => {
      monaco.languages.registerCompletionItemProvider(language, {
        provideCompletionItems: (model, position) => {
          // Check if the model is available
          if (model !== modelRef.current) {
            return null;
          }

          // Provide completion items
          return {
            suggestions: []
          };
        }
      });
    });

    // Listen for changes
    editorRef.current.onDidChangeModelContent(() => {
      onChange(editorRef.current!.getValue());
    });

    const setDimension = () => {
      setScreenSize({
        dynamicWidth: window.innerWidth,
        dynamicHeight: window.innerHeight
      });
    };
    window.addEventListener('resize', setDimension);

    // Cleanup function
    return () => {
      editorRef.current!.dispose();
      window.removeEventListener('resize', setDimension);
    };
  }, []);

  return (
    <div
      id="monaco-editor"
      style={{ height: height || screenSize.dynamicHeight, width: width || screenSize.dynamicWidth }}
    ></div>
  );
};

export default MonacoEditor;
