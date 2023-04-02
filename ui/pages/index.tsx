import { useState } from 'react';
import dynamic from 'next/dynamic';
import { upsertFile } from '../utils/db/client';
import { db } from '../utils/db/db.config';

const MonacoEditor = dynamic(() => import('../components/editor'), {
  ssr: false
});

const MyPage = () => {
  const [code, setCode] = useState<string>('import life;');
  let debounceTimeout : NodeJS.Timeout | undefined;

  const handleCodeChange = (content: string) => {
    setCode(content);
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout( async () => {
      const update = await upsertFile(db, "something", content);
    }, 1000);
  };

  return (
      <div>
        <MonacoEditor value={code} onChange={handleCodeChange} />
      </div>
  );
};

export default MyPage;
