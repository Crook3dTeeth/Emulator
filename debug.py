# Debugging file

# Output conversions
from logging import exception
from msilib.schema import Binary


system_raw = False
system_hex = False
system_int = True
system_cha = False


def debug(register_list, memory = [], extra_info = ""):
    for register in register_list:
        register_name, size, bus_width, data = register.printRegister()
        print("Register name: {0} :: Used Capacity: {1} ".format(register_name, RegisterCapacity(bus_width, size, data)))


def RegisterCapacity(bus_width, size, data = []):
    register_capacity = 0
    i = 0
    low_register = ""

    while i < bus_width:
        low_register += "0"
        i += 1

    for item in data:
        if item != low_register:
            register_capacity += 1

    return register_capacity


def debugPrint(data, extra_info = "", data1 = "", extra_info1 = "", raw_only = False):
    """Used to print debug info"""

    if raw_only:
        print("{0}{1}{2}{3}".format(extra_info, data, extra_info1, data1))

    else:
        if system_raw:
            print("{0}{1}{2}{3}".format(extra_info, data, extra_info1, data1))

        if system_int:
            int_data = str_to_binary(data)
            int_data1 = str_to_binary(data1)
            print("{0}{1}{2}{3}".format(extra_info, int_data, extra_info1, int_data1))

        if system_hex:
            int_data = str_to_binary(data)
            int_data1 = str_to_binary(data1)
            try:
                print("{0}{1}{2}{3}".format(extra_info, hex(int_data), extra_info1, hex(int_data1)))
            except:
                print("Not valid hex")

        if system_cha:
            int_data = str_to_binary(data)
            int_data1 = str_to_binary(data1)
            try:
                print("{0}{1}{2}{3}".format(extra_info, chr(int_data), extra_info1, chr(int_data1)))
            except:
                print("Not valid hex")


def str_to_binary(data):
    count = 0
    converted_int = 0
    for i in reversed(data):
        if i == "1":
            converted_int += 2 ** count
        elif i != "0":
            return "Error: Not a valid binary number"
        count += 1
    return converted_int

class c:
    class clear:
        pass
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class t:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class b:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

#region graphics

class mem_allocation_graphic():

    def __init__(self, bar_size, bg_color, txt_color, bg_text):
        self.bar_size = bar_size
        self.bg = bg_color
        self.txt = txt_color
        self.txtbg = bg_text
        self.bar_percentage = 0 # starting bars

        self.barline = ""
        i = 0
        while i < self.bar_size:
            self.barline += " "
            i += 1

    def print_bar(self):
        
        print(self.barline)
        pass

    def increase_bar(self, increase = 1):
        if self.bar_percentage < self.bar_size:
            self.barline = "=" * increase + self.barline
            self.barline = self.barline[:-1]
            self.bar_percentage += 1
            return False
        else:
            print("done")
            return True
            

#endregion
