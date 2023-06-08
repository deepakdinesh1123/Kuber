import { useState } from "react";
import styles from "styles/FileTree.module.css";

interface Node {
  type: "directory" | "file";
  name: string;
  path: string;
  children?: Node[];
}

interface FileTreeProps {
  data: Node[];
  click: (path: string, isDirectory: boolean) => void;
}

function FileTree({ data, click }: FileTreeProps) {
  const [expanded, setExpanded] = useState<string[]>([]);
  const [cur, setcur] = useState<string[]>([]);

  const handleToggle = (path: string, isDirectory: boolean) => {
    if (expanded.includes(path)) {
      setExpanded((prev) => prev.filter((p) => p !== path));
    } else {
      setExpanded((prev) => [...prev, path]);
    }
    click(path, isDirectory);
  };

  const addDirectory = () => {

  }

  const addFile = () => {

  }

  const renderTree = (nodes: Node[]) => {
    return nodes.map((node) => {
      const isDirectory = node.type === "directory";
      const path = node.path;

      const label = (
        <div
          className={styles.label}
          onClick={() => handleToggle(path, isDirectory)}
          style={{ paddingLeft: isDirectory ? 16 : 32 }}
        >
          <span className={styles.icon}>{isDirectory ? "📁" : "📄"}</span>
          <span className={styles.name}>{node.name}</span>
        </div>
      );

      if (isDirectory && expanded.includes(path)) {
        return (
          <div key={path}>
            {label}
            <div className={styles.children}>{renderTree(node.children!)}</div>
          </div>
        );
      }

      return <div key={path}>{label}</div>;
    });
  };

  return <>
    <button onClick={addDirectory}>Folder</button>
    <button onClick={addFile}>File</button>
    <div className={styles.container}>{renderTree(data)}</div>;
  </>
}

export default FileTree;
