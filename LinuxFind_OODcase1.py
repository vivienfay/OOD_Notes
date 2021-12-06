# Linux Find
from OOD_Notes.DesignAmazonLocker import Size


class File(object):
    def __init__(self, name, size, extension, isDirectory, children):
        self.name = name
        self.size = size
        self.extension = extension
        self.isDirectory = isDirectory
        self.children = children

class Filter(object):
    def __init__(self):
        pass
    
    def apply(self):
        pass

class SizeFilter(Filter):
    def __init__(self, size):
        self.size = size
    
    def apply(self, file):
        return file.size > self.size

class ExtensionFilter(Filter):
    def __init__(self, ext):
        self.extension = ext
    
    def apply(self, file):
        return file.extension == self.extension

class LinusFindSystem(object):
    def __init__(self):
        self.filters = []
    
    def addFilter(self, f):
        self.filters.append(f)
    
    def Find(self, root):
        def search(cur):
            if not cur.isDirectory:
                for filter in self.filters:
                    if not filter.apply(cur): break
                res.append(cur)
            for i in cur.children:
                search(i)
        res = []
        search(root)
        return res


