from importlib import import_module
import json
from os import path, getcwd
import os
import pathlib

from dsl.filemgr import FileManager
from dsl.fileop import FilterManager, FolderItem
from dsl.datatype import DataType
from dsl.accessrights import AccessRights
from dsl.exechelper import ExecHelper
from dsl.exceptions import ModuleNotFoundError

class Pair(object):
    def __init__(self, v1, v2):
        self.pair = (v1, v2)
    
    def __getitem__(self, key):
        return self.pair[key]
    
    def __iter__(self):
        return iter(self.pair)
        
def load_module(modulename):
    '''
    Load a module dynamically from a string module name.
    It was first implemented with __import__, but later
    replaced by importlib.import_module.
    :param modulename:
    '''
    #if modulename not in sys.modules:
    #name = "package." + modulename
    #return __import__(modulename, fromlist=[''])
    return import_module(modulename)
      
class LibraryBase():
    def __init__(self, filemanager: FileManager):
        self.tasks = {}
        self.localdir = path.join(path.abspath(path.dirname(__file__)), 'storage')
        self.filemanager = filemanager
    
    def add_task(self, name, expr):
        self.tasks[name] = expr
    
    def run_task(self, name, args, dotaskstmt):
        if name in self.tasks:
            return dotaskstmt(self.tasks[name][1:], args)

    def code_run_task(self, name, args, dotaskstmt):
        if name in self.tasks:
            return dotaskstmt(self.tasks[name], args), set()
           
    def check_function(self, name, package = None):
        return name.lower() in ["print",
            "read",
            "write",
            "getfiles",
            "getfolders",
            "createfolder",
            "remove",
            "makedirs",
            "getcwd",
            "isfile",
            "dirname",
            "basename",
            "getdatatype",
            "len",
            "exec",
            "copyfile",
            "deletefile"
        ]

    def check_functions(self, v):
        for f in v:
            if LibraryBase.check_function(f.name, f.package):
                return True
        return False            

    @staticmethod        
    def split_args(arguments):
        args = []
        kwargs = {}
        for arg in arguments:
            if isinstance(arg, Pair):
                kwargs[arg[0]] = arg[1]
            else:
                args.append(arg)
        return args, kwargs
    
    def GetDataTypeFromFunc(self, returns, result = None):
        if not returns:
            return DataType.Custom
        
        datatype = DataType.Unknown
        try:
            returnsLower = returns.lower().split('|')
            if 'file' in returnsLower:
                fs = FileManager.fs_by_prefix_or_default(str(result))
                if fs.isfile(result):
                    datatype = datatype | DataType.File
            elif 'folder' in returnsLower:
                fs = FileManager.fs_by_prefix_or_default(str(result))
                if fs.isdir(result):
                    datatype = datatype | DataType.Folder
            elif 'file[]' in returnsLower:
                if type(result) == 'list':
                    datatype = datatype | DataType.FileList
            elif 'folder[]' in returnsLower:
                if type(result) == 'list':
                    datatype = datatype | DataType.FolderList
            else:
                datatype = DataType.Custom
        except:
            pass # don't propagate the exceptions
        return datatype

    def check_access_rights(self, user_id, data, rights):
        print('Access right not checked')

    def call_func(self, context, package, function, args):
        '''
        Call a function from a module.
        :param context: The context for output and error
        :param package: The name of the package. If it's empty, local function is called    
        :param function: Name of the function
        :param args: The arguments for the function
        '''
        arguments, kwargs = LibraryBase.split_args(args)

        if function.lower() == "print":
            result = context.write(*arguments)
        elif function.lower() == "range":
            result = range(*arguments)
        elif function.lower() == "read":
            if not arguments:
                raise ValueError("Read must have one argument.")
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Read)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.read(arguments[0])
        elif function.lower() == "write":
            if len(arguments) < 2:
                raise ValueError("Write must have two arguments.")
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Write)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.write(arguments[0], arguments[1])
        elif function.lower() == "getfiles":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Read)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = FolderItem.StrToFolderItem(FilterManager.listdirR(fs, arguments[0], arguments[1], True)) if len(arguments) == 2 else FolderItem.StrToFolderItem(fs.get_files(arguments[0]))
        elif function.lower() == "getfolders":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Read)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.get_folders(arguments[0])
        elif function.lower() == "createfolder":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Write)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.makedirs(arguments[0])
        elif function.lower() == "remove":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Write)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.remove(arguments[0])
        elif function.lower() == "makedirs":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Write)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.makedirs(arguments[0])
        elif function.lower() == "getcwd":
            result = getcwd()
        elif function.lower() == "isfile":
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.isfile(arguments[0])
        elif function.lower() == "dirname":
            result = os.path.dirname(arguments[0])
        elif function.lower() == "basename":
            result = os.path.basename(arguments[0])
        elif function.lower() == "getdatatype":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Read)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            extension = pathlib.Path(arguments[0]).suffix
            result = extension[1:] if extension else extension
        elif function.lower() == "len":
            result = len(arguments[0])
        elif function.lower() == "exec":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Read)
            result = ExecHelper.func_exec_run(arguments[0], *arguments[1:])
        elif function.lower() == "copyfile":
            self.check_access_rights.check_access_rights(context.user_id, arguments[1], AccessRights.Write)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.copy(arguments[0], arguments[1])
        elif function.lower() == "deletefile":
            self.check_access_rights.check_access_rights(context.user_id, arguments[0], AccessRights.Write)
            fs = self.filemanager.fs_by_prefix_or_default(arguments[0])
            result = fs.remove(arguments[0])
        else:
            raise ModuleNotFoundError("Module not found in the database.", function)
        
        return result

    def code_func(self, context, package, function, arguments):
        '''
        Call a function from a module.
        :param context: The context for output and error
        :param package: The name of the package. If it's empty, local function is called    
        :param function: Name of the function
        :param arguments: The arguments for the function
        '''
        imports = set()
        args = ','.join(arguments)
        code = ''
        if not package or package == "None":
            if function.lower() == "print":
                code = "print({0})".format(args)
            elif function.lower() == "range":
                code = "range({0})".format(args)
            elif function.lower() == "read":
                imports.add("from fileop import IOHelper")
                code = "IOHelper.read({0})".format(args)
            elif function.lower() == "write":
                imports.add("from fileop import IOHelper")
                code = "IOHelper.write({0})".format(args)
            elif function.lower() == "getfiles":
                imports.add("from fileop import IOHelper")
                code = "IOHelper.getfiles({0})".format(args)
            elif function.lower() == "getfolders":
                imports.add("from fileop import IOHelper")
                code = "IOHelper.getfolders({0})".format(args)
            elif function.lower() == "remove":
                imports.add("from fileop import IOHelper")
                code = "IOHelper.remove({0})".format(args)
            elif function.lower() == "createfolder":
                imports.add("from fileop import IOHelper")
                code = "IOHelper.makedirs({0})".format(args)
            elif function.lower() == "getcwd":
                imports.add("import os")
                code = "os.getcwd()"
            elif function.lower() == "len":
                code = "len({0})".format(arguments[0])
            elif function.lower() == "exec":
                imports.add("import subprocess")
                code =  "func_exec_run({0}, {1})".format(arguments[0], arguments[1])

        if code:
            return code, imports
        
        imports.add("from importlib import import_module")
        func = self.get_function(function, package)
        code = "module_obj = load_module({0})\n".format(func[0].module)
        code += "function = getattr(module_obj, {0})\n".format(func[0].internal)
        if context.dci and context.dci[-1] and func.runmode == 'distibuted':
            args = [context.dci[-1]] + args
        code += "function({0})".format(args)
        return code, imports