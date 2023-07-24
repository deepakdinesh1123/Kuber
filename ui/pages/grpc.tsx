import { useState } from "react";
import { StyleRegistry } from "styled-jsx";
var {
  ExecuteRequest,
  ExecutionResponse,
} = require("../definitions/execution/execute_pb");
var { ExecuteClient } = require("../definitions/execution/execute_grpc_web_pb");

const client = new ExecuteClient("http://localhost:8080");

const MyPage = () => {
  const [text, setText] = useState("");

  const handleClick = () => {
    const executeRequest = new ExecuteRequest();
    executeRequest.setContainerName("nerdy-fuchsia-spider");
    executeRequest.setCommand("sh infy.sh");
    executeRequest.setDir("/");
    const stream = client.execute_command(executeRequest, {});

    stream.on("data", (response) => {
      const message = response.getMessage();
      console.log("Received message:", message);
    });

    stream.on("end", () => {
      console.log("Stream ended");
    });

    stream.on("error", (error) => {
      console.error("Error:", error.message);
    });
  };

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleClick}>Submit</button>
    </div>
  );
};

export default MyPage;
