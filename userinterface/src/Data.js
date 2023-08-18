import { fetchDataFromApi } from "./fetchData";

function isFile(name) {
  return name.includes(".");
}

function generateDataStructure(contents, parentId = 0) {
  const items = contents.split("\n").filter((item) => item.trim() !== "");

  return items.map((name, index) => {
    const _id = parentId + index + 1;
    const checked = 0;
    const isItemFile = isFile(name);

    return {
      name,
      _id,
      checked,
      isFile: isItemFile,
      icon: isItemFile ? "file-icon" : "folder-icon", // Use appropriate icons for files and folders
      expandable: !isItemFile, // Files should not be expandable
      children: isItemFile ? undefined : generateDataStructure("", _id * 1000), // Use a multiplier to differentiate between directory and file IDs
    };
  });
}

const path = "/";
const sandboxId = "123";
const containerId = "69b45518172c";
const apiResponse = await fetchDataFromApi(sandboxId, containerId, path);
console.log(apiResponse);
const generatedData = generateDataStructure(apiResponse.contents);
const testData = {
  name: "All Contents",
  _id: 0,
  checked: 0,
  expandable: true,
  children: generatedData,
};

export { testData };
