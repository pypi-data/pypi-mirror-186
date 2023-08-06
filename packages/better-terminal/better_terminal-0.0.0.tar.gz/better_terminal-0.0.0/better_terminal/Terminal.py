import os
import platform

class New:
    def __init__(self, template:str):
        self.template:str = template
        self.variables = list()
        self.__add_clear_terminal()
        self.__update_terminal()
    
    def update_template(self, new_template:str):
        self.template = new_template
        self.__update_terminal()
    
    def create_variable(self, name:str, valueData):
        variable = Variable(self.__update_terminal, name, valueData)
        self.variables.append(variable)
        self.__update_terminal()
        return variable
    
    def __update_terminal(self):
        string:str = self.template
        for variable in self.variables:
            string = string.replace("#{}#".format(variable.name), str(variable.valueData))

        for color in COLOR.values():
            color_code = COLOR_LOOKUP_TABLE.get(color.split("@")[1])
            string = string.replace(color, "\x1b[1;{}m".format(color_code))
        self.__clear_terminal()
        print(string, "\x1b[1;0m")
    
    def __add_clear_terminal(self):
        clear_command:str = "clear"
        if(platform.system() == "Windows"): clear_command = "clr"
        def clear_function():
            os.system(clear_command)
        self.__clear_terminal = clear_function


class Variable:
    def __init__(self, update_function, name:str, valueData):
        self.name:str = name
        self.valueData = valueData
        self.__update_function = update_function
    
    @property
    def value(self):
        return self.valueData
    
    def update(self, value):
        self.valueData = value
        self.__update_function()
COLOR = {
    "CLEAR":"@CLEAR@",
    "BLACK":"@BLACK@",
    "RED":"@RED@",
    "GREEN":"@GREEN@",
    "YELLOW":"@YELLOW@",
    "BLUE":"@BLUE@",
    "MAGENTA":"@MAGENTA@",
    "CYAN":"@CYAN@",
    "WHITE":"@WHITE@",
    "BRIGHT_BLACK":"@BRIGHT_BLACK@",
    "BRIGHT_RED":"@BRIGHT_RED@",
    "BRIGHT_GREEN":"@BRIGHT_GREEN@",
    "BRIGHT_YELLOW":"@BRIGHT_YELLOW@",
    "BRIGHT_BLUE":"@BRIGHT_BLUE@",
    "BRIGHT_MAGENTA":"@BRIGHT_MAGENTA@",
    "BRIGHT_CYAN":"@BRIGHT_CYAN@",
    "BRIGHT_WHITE":"@BRIGHT_WHITE@"
}

COLOR_LOOKUP_TABLE = {
    "CLEAR": 0,
    "BLACK": 30,
    "RED": 31,
    "GREEN": 32,
    "YELLOW": 33,
    "BLUE": 34,
    "MAGENTA": 35,
    "CYAN": 36,
    "WHITE": 37,
    "BRIGHT_BLACK": 90,
    "BRIGHT_RED": 91,
    "BRIGHT_GREEN": 92,
    "BRIGHT_YELLOW": 93,
    "BRIGHT_BLUE": 94,
    "BRIGHT_MAGENTA": 95,
    "BRIGHT_CYAN": 96,
    "BRIGHT_WHITE": 97
}