import os


class FileOrDirectory:
    @property
    def name(self):
        return self.path.split('/')[-1]

    @property
    def exists(self):
        return os.path.exists(self.path)

    def __eq__(self, other):
        print(self.path, other.path)
        if isinstance(self, type(other)):
            return self.path == other.path
        return False
