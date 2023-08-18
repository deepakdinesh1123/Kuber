import FolderTree, { testData } from "react-folder-tree";
//import { testData } from "./Data";

const BasicTree = () => {
  const onTreeStateChange = (state) => console.log("tree state: ", state);

  return (
    <FolderTree
      data={testData}
      onChange={onTreeStateChange}
      showCheckbox={false}
    />
  );
};

export default BasicTree;
