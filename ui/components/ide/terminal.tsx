import React, { useEffect, useRef, useState } from "react";
import "xterm/css/xterm.css";

const XtermComponent = () => {
  const terminalRef = useRef(null);
  let terminal;
  const [allowInput, setAllowInput] = useState(true);

  useEffect(() => {
    import("xterm").then((xterm) => {
      import("xterm-addon-fit").then((fitAddon) => {
        const { Terminal } = xterm;
        const { FitAddon } = fitAddon;

        terminal = new Terminal();
        const fitAddonInstance = new FitAddon();
        terminal.loadAddon(fitAddonInstance);

        terminal.open(terminalRef.current);
        fitAddonInstance.fit();

        const promptString = "$ ";
        let currentInput = "";

        terminal.onData((data) => {
          if (!allowInput) {
            return;
          }

          if (data === "\x7f") {
            if (currentInput.length > 0) {
              currentInput = currentInput.slice(0, -1);
              terminal.write("\b \b");
            }
          } else {
            terminal.write(data);

            if (data !== "\r") {
              currentInput += data;
            } else {
              handleCommand(currentInput.trim());
              currentInput = "";
              terminal.write("\r\n" + promptString);
            }
          }
        });

        terminal.write(promptString);

        return () => {
          terminal.dispose();
        };
      });
    });
  }, []);

  const handleCommand = (command) => {
    if (command.startsWith("echo ")) {
      const textToEcho = command.slice(5);
      terminal.write("\r\n" + textToEcho);
    } else if (command === "clear") {
      terminal.clear();
    }

    setAllowInput(false);

    const disableInputDuration = 1000;
    setTimeout(() => {
      setAllowInput(true);
    }, disableInputDuration);
  };

  return <div ref={terminalRef} style={{ height: "100vh" }} />;
};

export default XtermComponent;
