import { useRef, useEffect } from 'react';
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api';
import 'monaco-editor/esm/vs/basic-languages/python/python.contribution';
import 'monaco-editor/esm/vs/editor/editor.all.js';

type MonacoEditorProps = {
  value: string;
  onChange: (newValue: string) => void;
};


const MonacoEditor = ({ value, onChange }: MonacoEditorProps) => {
  const editorRef = useRef<monaco.editor.IStandaloneCodeEditor | null>(
    null
  );
  const models = useRef<Array<monaco.editor.ITextModel>>([]);

    monaco.languages.register({ id: 'python' });

    // Set up a completion provider for Python
    monaco.languages.registerCompletionItemProvider('python', {
    provideCompletionItems: (model, position) => {
        const textUntilPosition = model.getValueInRange({
        startLineNumber: 1,
        startColumn: 1,
        endLineNumber: position.lineNumber,
        endColumn: position.column
        });

        // TODO: Implement completion suggestions based on the code context

        return {
        suggestions: []
        };
    }
    });

    monaco.languages.setLanguageConfiguration("python", {
    comments: {
        lineComment: '#'
      },
      brackets: [
        ['{', '}'],
        ['[', ']'],
        ['(', ')']
      ],
      autoClosingPairs: [
        { open: '{', close: '}' },
        { open: '[', close: ']' },
        { open: '(', close: ')' },
        { open: "'", close: "'", notIn: ['string', 'comment'] },
        { open: '"', close: '"', notIn: ['string'] }
      ],
      surroundingPairs: [
        { open: '{', close: '}' },
        { open: '[', close: ']' },
        { open: '(', close: ')' },
        { open: "'", close: "'" },
        { open: '"', close: '"' }
      ],
      folding: {
        markers: {
          start: new RegExp("^\\s*#region\\b"),
          end: new RegExp("^\\s*#endregion\\b")
        }
    }
  });

  

  useEffect(() => {
    // initialize the Monaco editor
    editorRef.current = monaco.editor.create(
      document.getElementById('monaco-editor')!,
      {
        theme: 'vs-dark',
        model: null,
        language: "python",
      }
    );


    models.current.push(monaco.editor.createModel(value = "import shit"));
    editorRef.current.setModel(models.current[0]);

    // listen for changes
    editorRef.current.onDidChangeModelContent(() => {
      onChange(editorRef.current!.getValue());
    });


    // cleanup function
    return () => {
      editorRef.current!.dispose();
    };
  }, []);

  return (
    <div
      id="monaco-editor"
      style={{ height: '500px' }}
    ></div>

  );
};

export default MonacoEditor;
