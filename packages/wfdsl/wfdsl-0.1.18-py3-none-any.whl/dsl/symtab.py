class SymbolTable(object):
    '''
    Table to hold program symbols (vars).
    For local symbols, a stack of symbol tables is
    maintained.
    '''
    def __init__(self):
        '''
        Initializes the table.
        '''
        self.vars = {}
        
    def add_var(self, name, value):
        '''
        Adds/Overwrites a variable to the symbol table.
        :param name:
        :param value:
        '''
        self.vars[name] = value
        return self.get_var(name)
    
    def update_var(self, name, value):
        '''
        Updates a variable in the symbol table
        :param name:
        :param value:
        '''
        self.check_var(name)
        self.vars[name] = value
        return value
    
    def var_exists(self, name):
        '''
        Checks if a variable exists in the symbol table
        :param name:
        '''
        return name in self.vars
    
    def check_var(self, name):
        if not self.var_exists(name):
            raise ValueError("var {0} does not exist".format(name))
        return True
            
    def get_var(self, name):
        '''
        Gets value of a variable
        :param name:
        '''
        self.check_var(name)
        return self.vars[name]