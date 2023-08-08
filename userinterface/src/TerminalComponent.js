// TerminalComponent.js
import React from "react";
import { Terminal } from "react-terminal-component";

// External JavaScript function that will be used as a command handler
const handleCommand = (command, print) => {
  if (command === "hello") {
    print("Hello, world!");
  } else if (command === "date") {
    const currentDate = new Date().toLocaleDateString();
    print(`Current date is: ${currentDate}`);
  } else {
    print(`Unknown command: ${command}`);
  }
};

const TerminalComponent = () => {
  return (
    <Terminal
      commands={{
        hello: 'Prints "Hello, world!"',
        date: "Prints the current date",
      }}
      descriptions={{
        hello: 'Prints "Hello, world!"',
        date: "Prints the current date",
      }}
      commandPassThrough={(cmd, print) => handleCommand(cmd, print)}
      prompt=">"
    />
  );
};

export default TerminalComponent;
