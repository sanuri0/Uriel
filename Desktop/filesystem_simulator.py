class Node:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []

class FileSystem:
    def __init__(self):
        self.root = Node("/", is_directory=True)
        self.current_directory = self.root

    def ls(self):
        return "\n".join(child.name for child in self.current_directory.children)

    def mkdir(self, directory_name):
        new_directory = Node(directory_name, is_directory=True)
        self.current_directory.children.append(new_directory)

    def cd(self, directory_name):
        for child in self.current_directory.children:
            if child.is_directory and child.name == directory_name:
                self.current_directory = child
                return
        return "Directory not found."

    def touch(self, file_name):
        new_file = Node(file_name)
        self.current_directory.children.append(new_file)
        return f"File '{file_name}' created at {self.current_directory.name}"


# Example usage:
filesystem = FileSystem()
print(filesystem.ls())

filesystem.mkdir("documents")
filesystem.cd("documents")
print(filesystem.ls())

filesystem.touch("UrielSanchezresume.txt")
print(filesystem.ls())

filesystem.cd("..")
print(filesystem.ls())
