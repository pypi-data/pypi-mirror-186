import os
from os.path import join
import pathlib
import shutil
import sys
import tempfile
from urllib.parse import urlparse, urlunparse, urlsplit, urljoin
import uuid
import urllib
import re
from datetime import datetime
import threading

__author__ = "Mainul Hossain"
__date__ = "$Dec 10, 2016 2:23:14 PM$"

class FolderItem():
    def __init__(self, path):
        self.path = path
    
    def __str__(self):
        return self.path
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return FolderItem.union(self.path, other)
    
    def __sub__(self, other):
        return FolderItem.substract(self.path, other)
        
    @staticmethod
    def StrToFolderItem(item_s):
        return [FolderItem(f) for f in item_s] if isinstance(item_s, list) else FolderItem(item_s)
    
#     @staticmethod
#     def union(left, right):
#         v = []
#         if not isinstance(left, list):
#             left = [left]
#             
#         if not isinstance(right, list):
#             right = [right]
#         
#         rest = []
#         for l in left:
#             rest = [r for r in right if str(l) != str(r)]
#         left.extend(rest)
#         return left
    
    # set operations  
    @staticmethod
    def union(left, right):
        if not isinstance(left, list):
            left = [left]
             
        if not isinstance(right, list):
            right = [right]
         
        left = [str(f) for f in left]
        right = [str(f) for f in right]
        left_s = set(left)
        right_s = set(right)
         
        left = left_s.union(right_s)
        return [FolderItem(f) for f in left]
      
#     @staticmethod
#     def substract(left, right):
#         if not isinstance(left, list):
#             left = [left]
#             
#         if not isinstance(right, list):
#             right = [right]
#             
#         for r in right:
#             left = [l for l in left if str(l) != str(r)]
#             
#         return left
    
    
    @staticmethod
    def substract(left, right):
        if not isinstance(left, list):
            left = [left]
             
        if not isinstance(right, list):
            right = [right]
         
        left = [str(f) for f in left]
        right = [str(f) for f in right]
        left_s = set(left)
        right_s = set(right)
         
        left = left_s - right_s
        return [FolderItem(f) for f in left]                    
    
class FilterManager:
    @staticmethod
    def Filter(fs, path, filename, filters):
        for fil in filters:
            if not fil['selected']:
                continue
            name = fil['name'].lower()
            if name == "name":
                if not FilterManager.CheckRegExValue(fil['value'], filename):
                    return None
            elif name == "created" or name == "modified" or name == "accessed" or name == "size":
                stat = fs.stat(fs.join(path, filename))
                if name == "size":
                    if not FilterManager.SizeInRange(stat.st_size, fil['value']):
                        return None
                else:
                    t = None
                    if name == "created":
                        t = stat.st_ctime
                    elif name == "modified":
                        t = stat.st_mtime
                    else:
                        t = stat.st_atime
                    if not FilterManager.DateInRange(t, fil['value']):
                        return None
            elif name == "key:value":
                pass
            
        return filename

    @staticmethod
    def CheckRegExValue(regexvalue, value):
        return re.search(regexvalue, value, flags=re.RegexFlag.IGNORECASE)
        
    @staticmethod
    def DateInRange(dateV, dateR):
        begin_end = FilterManager.SplitDateRange(dateR)
        if not begin_end:
            return True
        if dateV < datetime.timestamp(begin_end[0]):
            return False
        if len(begin_end) > 1 and  dateV > datetime.timestamp(begin_end[1]):
            return False
        return True
    
    @staticmethod
    def SizeInRange(sizeV, sizeR):
        sizeR = sizeR.replace(" KB", "")
        begin_end = sizeR.split(",")
        if not begin_end:
            return True
        if sizeV < int(begin_end[0]) * 1024:
            return False
        if len(begin_end) > 1 and  sizeV > int(begin_end[1]) * 1024:
            #print_len = len(begin_end)
            #print_endSize = int(begin_end[1]) * 1024
            return False
        return True
    
    @staticmethod
    def SplitDateRange(dateR):
        begin_end = dateR.split('-')
        return [datetime.strptime(begin_end[0].strip(), '%m/%d/%Y'), datetime.strptime(begin_end[1].strip(), '%m/%d/%Y')] 

    @staticmethod
    def Sort(fs, filenames, filters):
        for fil in filters:
            if fil['selected'] and fil['sort']:
                name = fil['name'].lower()
                if name == "name":
                    filenames = sorted(filenames, reverse = (int(fil['sort'])==2))
        return filenames
    
    @staticmethod
    def listdirR(fs, path, filters, flatfiles = False):
        
        ancestors = FilterManager.listdirRInternal(fs, path, filters, flatfiles)
        if not ancestors:
            return None
        
        if flatfiles:
            return ancestors
        
        ancestorPath = path
        while fs.dirname(ancestorPath) and fs.strip_root(ancestorPath) != os.sep:
            ancestorPath = fs.dirname(ancestorPath) 
            ancestor = fs.make_json_item(ancestorPath)
            if fs.strip_root(ancestorPath) == os.sep:
                ancestor['text'] = fs.prefix
            ancestor['children'].append(ancestors)
            ancestors = ancestor
                
        return ancestors
            
    @staticmethod
    def listdirRInternal(fs, path, filters, flatfiles = False):
        if fs.isfile(path):
            filtered_file = filter(path, filters)
            if not filtered_file:
                return None
            
            return fs.make_json_item(path) if not flatfiles else path

        fsitems = []
        for fd in fs.get_folders(path):
            fditem = FilterManager.listdirRInternal(fs, fs.join(path, fd), filters, flatfiles)
            if fditem:
                fsitems.append(fditem)
        
        filter_active = any(f['selected'] for f in filters)
        fitems = []
        for f in fs.get_files(path):
            filename = fs.basename(f)
            if not filter_active or FilterManager.Filter(fs, path, filename, filters):
                fitems.append(filename)
                
        if fitems:
            fitems = FilterManager.Sort(fs, fitems, filters)
            for fitem in fitems:
                if flatfiles:
                    fsitems.append(fs.join(path, fitem))
                else:
                    fsitems.append(fs.make_json_item(fs.join(path, fitem)))
        
        if fsitems and not flatfiles:
            data_json = fs.make_json_item(path)
            data_json['children'] = fsitems
            data_json['loaded'] = True
            fsitems = data_json
            
        return fsitems
        
class BaseFileSystem(object):
    def __init__(self, root, public, temp, prefix):
        self.__lock = threading.Lock()
        self._localdir = root
        self.prefix = prefix
        self.public = public
        self.url = '/'
        self.temp = temp
    
    @property
    def localdir(self):
        return self._localdir
    @localdir.setter
    def localdir(self, dir):
        self.__lock.acquire()
        try:
            self._localdir = dir
        finally:
            self.__lock.release()
        
    def is_parent_of(self, parent, child):
        parent = self.normalize_path(parent)
        child = self.normalize_path(child)
        return child.startswith(parent)

    def normalize_fullpath(self, path):
        return self.normalize_path(path)
    
    def mkdir(self, path):
        raise ValueError("Not implemented error.")
    
    def remove(self, path):
        raise ValueError("Not implemented error.")
    
    def rename(self, oldpath, newpath):
        raise ValueError("Not implemented error.")
    
    def get_files(self, path):
        raise ValueError("Not implemented error.")
    
    def get_folders(self, path):
        raise ValueError("Not implemented error.")
    
    def listdir(self, path):
        raise ValueError("Not implemented error.")
    
    def listdirR(self, path, filters):
        raise ValueError("Not implemented error.")
    
    def copyfile(self, src, dst):
        raise ValueError("Not implemented error.")
                
    def read(self, path):
        raise ValueError("Not implemented error.")
    
    def write(self, path, content):
        raise ValueError("Not implemented error.")
        
    def unique_filename(self, path, prefix, ext):
        raise ValueError("Not implemented error.")
    
    def make_unique_dir(self, path):
        raise ValueError("Not implemented error.")
            
    def exists(self, path):
        raise ValueError("Not implemented error.")
        
    def isdir(self, path):
        raise ValueError("Not implemented error.")
    
    def isfile(self, path):
        raise ValueError("Not implemented error.")
    
    def join(self, path1, path2):
        raise ValueError("Not implemented error.")
    
    def basename(self, path):
        raise ValueError("Not implemented error.")
    
    #check again
    def dirname(self, path):
        raise ValueError("Not implemented error.")

    def make_json(self, path):
        raise ValueError("Not implemented error.")
    
    def make_json_r(self, path):
        raise ValueError("Not implemented error.")

    def save_upload(self, file, path):
        raise ValueError("Not implemented error.")
    
    def download(self, path):
        raise ValueError("Not implemented error.")
    
    def stat(self, path):
        raise ValueError("Not implemented error.")

    def unique_fs_name(self, path, prefix, ext):
        make_fn = lambda i: os.path.join(path, '{0}({1}){2}'.format(prefix, i, ext))

        for i in range(1, sys.maxsize):
            uni_fn = make_fn(i)
            if not self.exists(uni_fn):
                return uni_fn

class PosixFileSystem(BaseFileSystem):
    
    def __init__(self, root, public = None, temp = None, prefix = None):
        super().__init__(root, public, temp, prefix)
    
    def typename(self):
        return "posix"
        
    def normalize_path(self, path):
        path = os.path.normpath(path)
        if self.prefix:
            path = self.strip_prefix(path)
        if not self._localdir or path.startswith(self._localdir) or (self._localdir.endswith(os.sep) and path == self._localdir[:-1]):
            return path
        while path and path[0] == os.sep:
            path = path[1:]    
        return os.path.join(self._localdir, path)
    
    def makedirs(self, path):
        path = self.normalize_path(path)
        if not os.path.exists(path):
            os.makedirs(path)
        return self.make_prefix(path)
    
    def make_prefix(self, path):
        if not self.prefix:
            return path     
        if path.startswith(self.prefix):
            return path
        if path.startswith(self._localdir):
            path = path[len(self._localdir):]
        if not path.startswith(os.sep):
            path = os.sep + path
        return self.prefix + path
    
    def make_url(self, path):
        path = self.strip_prefix(path) 
        if self._localdir and path.startswith(self._localdir):
            path = path[len(self._localdir):]
        return path if path.startswith(os.sep) else os.sep + path
    
    def strip_prefix(self, path):
        return path[len(self.prefix):] if self.prefix and path.startswith(self.prefix) else path
        
    def strip_root(self, path):
        path = self.strip_prefix(path)
        if path.startswith(self._localdir):
            path = path[len(self._localdir):]
        return path if path.startswith(os.sep) else os.sep + path
            
    def mkdir(self, path):
        path = self.normalize_path(path)
        if not os.path.exists(path):
            os.mkdir(path) 
        return self.make_prefix(path)
    
    def remove(self, path):
        path = self.normalize_path(path)
        dirpath = os.path.dirname(path)
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        return self.make_prefix(dirpath)
               
    def rename(self, oldpath, newpath):
        oldpath = self.normalize_path(oldpath)
        newpath = self.join(self.dirname(oldpath), newpath)
        newpath = self.normalize_path(newpath)
        
        if oldpath == newpath:
            return oldpath
        
        os.rename(oldpath, newpath)
        return self.strip_root(newpath)
    
    def get_files(self, path):
        path = self.normalize_path(path)
        return [self.strip_root(os.path.join(path, f)) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    def get_folders(self, path):
        path = self.normalize_path(path)
        return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    
    def listdir(self, path):
        path = self.normalize_path(path)
        return os.listdir(path)
    
    def listdirR(self, path, filters):
        filters = filters if not filters or type(filters) is list else [filters]
        return FilterManager.listdirR(self, path, filters)
       
    def copyfile(self, src, dst):
        return shutil.copy2(self.normalize_path(src), self.normalize_path(dst))
    
    def stat(self, path):
        return os.stat(self.normalize_path(path))
    
    def read(self, path):
        path = self.normalize_path(path)
        with open(path, 'rb') as reader:
            return reader.read()
        
    def write(self, path, content):
        path = self.normalize_path(path)
        with open(path, 'wb') as writer:
            return writer.write(content)
        
    def unique_filename(self, path, prefix, ext):
        stem = pathlib.Path(prefix).stem
        if not ext:
            ext = pathlib.Path(prefix).suffix
        make_fn = lambda i: self.join(path, '{0}_{1}.{2}'.format(stem, i, ext) if ext else '{0}_{1}'.format(stem, i))

        for i in range(1, sys.maxsize):
            uni_fn = make_fn(i)
            if not self.exists(uni_fn):
                return uni_fn
    
    def make_unique_dir(self, path):
        unique_dir = self.join(path, str(uuid.uuid4()))
        unique_dir = self.normalize_path(unique_dir)
        os.makedirs(unique_dir)
        return unique_dir
            
    def exists(self, path):
        return os.path.exists(self.normalize_path(path))
        
    def isdir(self, path):
        return os.path.isdir(self.normalize_path(path))
    
    def isfile(self, path):
        return os.path.isfile(self.normalize_path(path))
    
    def join(self, path1, path2):
        path1 = self.normalize_path(path1)
        return self.make_url(os.path.join(path1, path2))
    
    def get_json_name(self, path):
        if (self._localdir and self._localdir == path) or path == os.sep:
            return self.prefix if self.prefix else self._localdir 
        
        return self.basename(path)
        
    def make_json_item(self, path):
        data_json =  { 'path': self.make_url(path), 'text': self.get_json_name(path) }
        if self.isdir(path):
            data_json['children'] = []
            data_json['type'] = 'folder'
        else:
            data_json['type'] = 'file'
        return data_json
        
    def make_json(self, path):
        data_json = self.make_json_item(path)
        
        if 'children' in data_json: # folder
            data_json['children'] = [self.make_json_item(self.join(path, fn)) for fn in self.listdir(path)]
            data_json['loaded'] = True
        return data_json
    
    def make_json_r(self, path):
        data_json = self.make_json_item(path)  
        if 'children' in data_json: # folder 
            data_json['children'] = [self.make_json_r(self.join(path, fn)) for fn in self.listdir(path)]
            data_json['loaded'] = True
        return data_json

    def save_upload(self, file, path):
        path = self.normalize_path(path)
        if self.isfile(path):
            path = os.path.dirname(path)
        elif not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, file.filename)
        file.save(path)
        return self.strip_root(path)
    
    def download(self, path):
        path = self.normalize_path(path)
        return path if os.path.isfile(path) else None
    
    def basename(self, path):
        path = self.normalize_path(path)
        return os.path.basename(path)
    
    #check again
    def dirname(self, path):
        path = self.strip_root(path)
        return os.path.dirname(path) if path.startswith('/') else path