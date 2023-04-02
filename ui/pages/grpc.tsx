import { useState } from 'react';
var {ExecuteRequest, ExecutionResponse } = require("../grpc-client/execution/execute_pb");
var { ExecuteClient } = require("../grpc-client/execution/execute_grpc_web_pb");

const client = new ExecuteClient("http://localhost:8080", null, null);

const MyPage = () => {
  const [text, setText] = useState('');

  const handleClick = () => {
    const executeRequest = new ExecuteRequest();
    executeRequest.setContainerName("Something");
    executeRequest.setCommand("ls");
    console.log(executeRequest);
    client.executeCommand(executeRequest, null, (err: any, response: any) => {
      if (err) return console.log(err);
      // const error = response.getError();
      // const msg = response.getMsg();
      console.log(response.getSuccess());
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