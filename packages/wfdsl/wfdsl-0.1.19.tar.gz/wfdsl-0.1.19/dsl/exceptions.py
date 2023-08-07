class WfDSLError(Exception):
    pass

class ModuleNotFoundError(WfDSLError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.module = kwargs.get('module')