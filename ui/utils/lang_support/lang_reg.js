import * as monaco from 'monaco-editor/esm/vs/editor/editor.api';

export function registerfileLanguage() {
  monaco.languages.register({ id: 'dockerfile' });
  monaco.languages.setMonarchTokensProvider('dockerfile', {
    tokenizer: {
      root: [
        [/^#.*$/, 'comment'],
        [
          /(FROM|MAINTAINER|RUN|CMD|EXPOSE|ENV|ADD|COPY|ENTRYPOINT|VOLUME|USER|WORKDIR|ARG|ONBUILD|LABEL)\b/,
          'keyword',
        ],
        [/".*?"/, 'string'],
        [/'[^']*'/, 'string'],
        [/[0-9]+/, 'number'],
        [/[A-Za-z0-9_-]+/, 'identifier'],
      ],
    },
  });

  // Register Rust language
  monaco.languages.register({
    id: 'rust',
    extensions: ['.rs'],
    aliases: ['Rust', 'rust'],
    mimetypes: ['text/x-rust-source', 'text/rust'],
  });
  monaco.languages.setMonarchTokensProvider('rust', {
    tokenizer: {
      root: [
        [/\/\/.*$/, 'comment'],
        [/\b(?:fn|let|if|else|while|loop|for|match|struct|enum|mod|use|pub|impl|trait|type|where|as|break|continue|return|crate|super|unsafe|extern|const|static|mut|ref|self|Self|true|false|null|Some|None)\b/, 'keyword'],
        [/[A-Za-z_][A-Za-z0-9_]*/, 'identifier'],
        [/\d+/, 'number'],
        [/".*?"/, 'string'],
      ],
    },
  });

   // Register Go language
   monaco.languages.register({
    id: 'go',
    extensions: ['.go'],
    aliases: ['Go', 'go'],
    mimetypes: ['text/x-go'],
  });
  monaco.languages.setMonarchTokensProvider('go', {
    tokenizer: {
      root: [
        [/\/\/.*$/, 'comment'],
        [/\b(?:package|import|func|var|const|type|struct|interface|map|chan|go|defer|if|else|for|range|switch|case|default|select|break|continue|fallthrough|return)\b/, 'keyword'],
        [/[A-Za-z_][A-Za-z0-9_]*/, 'identifier'],
        [/\d+/, 'number'],
        [/".*?"/, 'string'],
      ],
    },
  });
}
