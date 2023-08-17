// let a = {
//   tokenizer: {
//     root: [
//       // comments
//       [/^#.*$/, "comment"],
//       // keywords
//       [
//         /(FROM|FROM\w*|RUN|CMD|LABEL|EXPOSE|ENV|ADD|COPY|ENTRYPOINT|VOLUME|USER|WORKDIR|ONBUILD)\b/,
//         "keyword",
//       ],
//       // variables
//       [/\$(\{[^}]+\}|[A-Za-z0-9_]+)/, "variable"],
//       // labels
//       [/^\w+(?=\:)/, "label"],
//       // string literals
//       [/"([^"\\]|\\.)*$/, "string.invalid"],
//       [/'([^'\\]|\\.)*$/, "string.invalid"],
//       [/"/, "string", "@string_double"],
//       [/'/, "string", "@string_single"],
//       // numbers
//       [/\d+\.\d+/, "number.float"],
//       [/\d+/, "number"],
//       // delimiter
//       [/[:=\[\]{}\(\),]/, "delimiter"],
//       // whitespace
//       { include: "@whitespace" },
//     ],
//     string_double: [
//       [/[^\\"]+/, "string"],
//       [/\\./, "string.escape.invalid"],
//       [/"/, "string", "@pop"],
//     ],
//     string_single: [
//       [/[^\\']+/, "string"],
//       [/\\./, "string.escape.invalid"],
//       [/'/, "string", "@pop"],
//     ],
//     whitespace: [
//       [/[ \t\r\n]+/, ""],
//       [/\\\r?\n/, ""],
//     ],
//   },
// };

// console.log(typeof a);

// son = JSON.stringify(a);
// console.log(son);

class A {}
