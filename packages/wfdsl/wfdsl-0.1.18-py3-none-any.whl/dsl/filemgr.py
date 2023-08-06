from dsl.fileop import PosixFileSystem

class FileManager(object):
    
    @staticmethod
    def fs_by_typename(typename):
        if typename == 'posix':
            return PosixFileSystem(url, public, name)
        
        raise ValueError("File system not available")
    
    @staticmethod
    def ds_by_prefix(path):
        raise NotImplementedError()
    
    @staticmethod
    def fs_by_prefix_or_default(path):
        return FileManager.fs_by_typename("posix")       