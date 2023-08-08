import React, { useEffect, useRef, useState } from "react";
import { Terminal } from "xterm";
import { FitAddon } from "xterm-addon-fit";
import "xterm/css/xterm.css";

const XtermComponent = () => {
  const terminalRef = useRef(null);
  let terminal;
  const [allowInput, setAllowInput] = useState(true); // Use useState to define allowInput

  useEffect(() => {
    // Create a new terminal instance
    terminal = new Terminal();

    // Add fit addon to auto-resize the terminal with the window
    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    terminal.open(terminalRef.current);
    fitAddon.fit();

    // Set the prompt string
    const promptString = "$ ";
    let currentInput = "";

    // Attach event listener for handling key input
    terminal.onData((data) => {
      // If input is not allowed, do nothing
      if (!allowInput) {
        return;
      }

      // Handle backspace
      if (data === "\x7f") {
        if (currentInput.length > 0) {
          currentInput = currentInput.slice(0, -1);
          terminal.write("\b \b"); // Move cursor back, write space to clear, move cursor back again
        }
      } else {
        // Echo user input
        terminal.write(data);

        // Handle user input and store it
        if (data !== "\r") {
          currentInput += data;
        } else {
          // Enter was pressed, handle the command here
          handleCommand(currentInput.trim());
          currentInput = ""; // Clear current input
          terminal.write("\r\n" + promptString);
        }
      }
    });

    // Initialize the terminal with the prompt
    terminal.write(promptString);

    // Handle window resize to update terminal size
    const handleResize = () => {
      fitAddon.fit();
    };

    window.addEventListener("resize", handleResize);

    // Clean up on component unmount
    return () => {
      window.removeEventListener("resize", handleResize);
      terminal.dispose();
    };
  }, []);

  const handleCommand = (command) => {
    // Implement your command handling logic here

    // Check if the command is "echo"
    if (command.startsWith("echo ")) {
      const textToEcho = command.slice(5); // Extract the text after "echo "
      terminal.write("\r\n" + textToEcho); // Echo the text in a new line
    } else {
      // For demonstration purposes, we'll just log the command if it's not "echo"
      console.log(`Command executed: ${command}`);
    }

    // Disable input on previous lines after executing the command
    setAllowInput(false);

    // Wait for a moment (you can adjust the duration as needed)
    const disableInputDuration = 1000; // milliseconds
    setTimeout(() => {
      setAllowInput(true); // Enable input again
    }, disableInputDuration);
  };

  return <div ref={terminalRef} style={{ height: "100vh" }} />;
};

export default XtermComponent;
