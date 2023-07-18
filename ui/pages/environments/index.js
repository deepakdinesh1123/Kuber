import FileTree from "@/components/ide/fileTree";

const stories = () => {
  const fileData = [
    {
      type: "directory",
      name: "src",
      path: "/src",
      children: [
        {
          type: "directory",
          name: "components",
          path: "/src/components",
          children: [
            {
              type: "file",
              name: "Header.tsx",
              path: "/src/components/Header.tsx",
            },
            {
              type: "file",
              name: "Footer.tsx",
              path: "/src/components/Footer.tsx",
            },
          ],
        },
        {
          type: "directory",
          name: "pages",
          path: "/src/pages",
          children: [
            {
              type: "file",
              name: "IndexPage.tsx",
              path: "/src/pages/IndexPage.tsx",
            },
            {
              type: "file",
              name: "AboutPage.tsx",
              path: "/src/pages/AboutPage.tsx",
            },
          ],
        },
      ],
    },
    {
      type: "file",
      name: "package.json",
      path: "/package.json",
    },
    {
      type: "file",
      name: "README.md",
      path: "/README.md",
    },
  ];

  return (
    <>
      <FileTree data={fileData} />
    </>
  );
};

export default stories;
