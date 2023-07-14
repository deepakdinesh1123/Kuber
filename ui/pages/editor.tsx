import { useState } from "react";
import dynamic from "next/dynamic";
import { upsertFile } from "../utils/db/client";
import { db } from "../utils/db/db.config";

const MonacoEditor = dynamic(() => import("../components/ide/editor"), {
  ssr: false,
});

const Editor = () => {
  const [code, setCode] = useState<string>("import life;");
  let debounceTimeout: NodeJS.Timeout | undefined;

  const handleCodeChange = (content: string) => {
    setCode(content);
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(async () => {
      const update = await upsertFile(db, "something", content);
    }, 1000);
  };

  return (
    <div>
      <MonacoEditor
        value={code}
        onChange={handleCodeChange}
        language="Docker"
      />
    </div>
  );
};

export default Editor;
