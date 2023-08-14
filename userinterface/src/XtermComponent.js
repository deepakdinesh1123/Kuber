import React, { useEffect, useRef, useState } from "react";
import { Terminal } from "xterm";
import { FitAddon } from "xterm-addon-fit";
import "xterm/css/xterm.css";
import io from "socket.io-client";

const XtermComponent = ({ container, workdir }) => {
  const terminalRef = useRef(null);
  let terminal;
  const [allowInput, setAllowInput] = useState(true); // Use useState to define allowInput
  const cmd_exec = useRef(false);
  const promptString = `${workdir.current}#`;
  const socket = useRef(null);

  useEffect(() => {
    // Create a new terminal instance
    terminal = new Terminal();

    // Add fit addon to auto-resize the terminal with the window
    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    terminal.open(terminalRef.current);
    fitAddon.fit();

    // Set the prompt string
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
          console.log(currentInput.trim());
          currentInput = ""; // Clear current input
          if (!cmd_exec.current) {
            terminal.write("\r\n" + promptString);
          }
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
    terminal.write("\r\n");
    // Implement your command handling logic here

    // Check if the command is "echo"
    // if (command.startsWith("echo ")) {
    //   const textToEcho = command.slice(5); // Extract the text after "echo "
    //   terminal.write("\r\n" + textToEcho); // Echo the text in a new line
    // } else {
    //   // For demonstration purposes, we'll just log the command if it's not "echo"
    //   console.log(`Command executed: ${command}`);
    // }

    // // Disable input on previous lines after executing the command
    // setAllowInput(false);

    // // Wait for a moment (you can adjust the duration as needed)
    // const disableInputDuration = 1000; // milliseconds
    // setTimeout(() => {
    //   setAllowInput(true); // Enable input again
    // }, disableInputDuration);
    // 1. Create a WebSocket connection
    if (cmd_exec.current == false) {
      socket.current = new WebSocket("ws://localhost:8000/sandbox/process");

      // 2. Send an initial message
      socket.current.onopen = () => {
        const message = JSON.stringify({
          container_name: container,
          command: command,
          dir: workdir.current,
        });
        socket.current.send(message);
        cmd_exec.current = true;
      };
    } else {
      print(cmd_exec.current);
      socket.current.send(JSON.stringify({ action: "stdin", input: command }));
    }

    // 3. Set up a periodic task
    const readOutput = setInterval(() => {
      const readMessage = JSON.stringify({
        action: "read",
      });
      if (socket.readyState === WebSocket.OPEN) {
        socket.current.send(readMessage);
      } else {
        clearInterval(readOutput);
      }
    }, 1000);

    // 4. Receive messages
    socket.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.out != undefined) {
        terminal.write(data.out);
      }
    };

    // 5. Handle disconnection if needed
    socket.current.onclose = () => {
      cmd_exec.current = false;
      terminal.write(`\r\n${promptString}`);
      socket.current = null;
    };
  };

  return <div ref={terminalRef} style={{ height: "100vh" }} />;
};

export default XtermComponent;
