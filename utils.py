import os
import re


def add_import_statement(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
        pattern = r"^\s*import\s+.*?grpc.*?;$"
        match = re.search(pattern, contents, re.MULTILINE)
        if match:
            import_statement = match.group()
            updated_import = import_statement.replace("import", "import from defs", 1)
            contents = contents.replace(import_statement, updated_import)

    with open(file_path, "w") as file:
        file.write(contents)


def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".py"):
                add_import_statement(file_path)


# Provide the directory path here
directory_path = "/path/to/directory"
process_directory(directory_path)


def remove_migrations():
    folders = os.listdir("./rest")
    for folder in folders:
        if os.path.exists(f"./rest/{folder}/migrations"):
            for obj in os.listdir(f"./rest/{folder}/migrations"):
                if (
                    os.path.isfile(f"./rest/{folder}/migrations/{obj}")
                    and obj != "__init__.py"
                ):
                    os.remove(f"./rest/{folder}/migrations/{obj}")
