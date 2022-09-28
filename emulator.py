
# Architect
#region




# System Info
from doctest import OutputChecker
from operator import contains
from os import system
from pickle import NONE
from threading import excepthook
from debug import*
from instructionSet import*
from screenGraphics import*


display_sizeX = 854
display_sizeY = 480


#===========================#
# System Debug Options
system_debug = True # Extra output info

#===========================#


# System specs
num_registers = 4
clock_rate = 100 # Hz, 0 for step clock with printed output if system_debug is true
#mem options
mem_bus_width = 32
mem_size = 1024 * mem_bus_width     # Bytes
preallocate_memory = False


#filesystem
kernal = "C:/Users/tomkr/OneDrive/Documents/PCProject/EmulatorKernal/kernal.txt"
r_path = "C:/Users/tomkr/OneDrive/Documents/PCProject/EmulatorKernal/"

# Read/process
def openFile(filename):
    with open(filename) as file:
        for line in file: 
            print(line.rstrip())
            performAction(line.rstrip())
            input()


def performAction(line):
    pass


# Load Kernal

def loadKernal(kernal_path):
    #puts the kernal into memory for booting
    pass


# Clock starts from mem address 0
def start_clock(clock_speed):
    while True:
        pass

def step_clock():
    input()


#region Registers

class Registers:

    def __init__(self, size, bus_width, name, pre_allocate = False):
        self.name = name
        self.size = size
        self.busW = bus_width
        self.data = []

    def __len__(self):
        """ Returns the number of items in the stack """
        return len(self.data)

    def push(self, item):
        itemLength = len(item)
        if itemLength == self.busW:
            self.data.append(item)

        elif itemLength < self.busW:
            length_short = self.busW - itemLength
            i = 0
            item_addition = ""
            while i < length_short:
                item_addition += "0"
                i += 1
            new_data = (item_addition+item)
            self.data.append(new_data)
            if system_debug:
                debugPrint(new_data, "Push: ")     

    def pop(self):
        data = self.data.pop()
        if system_debug:
            print("Pop: ", data, " from register: ", self.name)

    def verifyAction(self, item, action):
        print("verify")

    def is_empty(self):
        """ Returns True if empty """
        return len(self.data) == 0

    def printRegister(self):
        """Prints an output of the register"""
        return self.name, self.size, self.busW, self.data

#endregion


# Memory
def MEMSetup():
    try:
        MEM = memory(mem_bus_width, mem_size)
        debugPrint(mem_size//8, "MEMSetup successfully || size: ", mem_bus_width, " Bytes || bus width: ", True)
    except:
        print("MEM Setup failed")
    return MEM


class memory:
    def __init__(self, bus_width, size):
        self.busW = bus_width
        self.size = size
        self.data = []

    def read(self, address):
        pass

    def write(self, address):
        pass 

    def address_finder(self, address):
        pass
        return 

    def allocate_memory(self, allocation_percentage):
        i = 0
        zero_line = ""
        mem_length = mem_size / mem_bus_width

        while i < self.busW:
            zero_line += "0"
            i += 1
        
        

        pass


# ALU
def ALUSetup():
    print("ALUSetup")

class BUS():
    def __init__(self):
        self.width = mem_bus_width
        self.items = b"0" * self.width
        self.openItems = []
        self.outputObject = []
        self.closedItems = []
        debugPrint(self.width, "Bus of width: ",  " Successfully created", "", True)

    def addItem(self, object):
        pass

    def removeItem(self, object):
        if object == self.outputObject:
            self.items = b"0" * self.width
            self.outputObject = []

    def openBus(self, object):
        if object == self.outputObject:
            self.openItems = []
            self.closedItems = []

    def readBus(self, object):
        if object in self.openItems:
            return self.items

    def lockBus(self, items = [], append = False, priority = False):
        if priority:
            if append:
                self.openItems.append(items)
            else:
                self.openItems = items
        else:
            if append:
                self.openItems.append(items)
            else:
                self.openItems = items


    def contains(self, item):
        for items in self.items:
            if items == item:
                return True
        return False

    def __contains__(self, item):
        return contains(item)

    def __str__(self):
        if system_debug:
            print("\nBus of width: " + str(self.width))
            print("Bus Items: " + str(self.items))
            print("Open items: ")
            return ""

        return str(self.items)


# PCIE (filesystem)

# VideoOutput

def main():
    try:
        MEM = MEMSetup()
        
    except:
        print("Failed to setup Memory")

    try:
        ALUSetup()
    except:
        print("Failed to setup ALU")

    if clock_rate == 0:
        step_clock()
    else:
        start_clock(clock_rate)
    #openFile(kernal)




def testFunc():
    bus = BUS()
    print(bus)


#main()
testFunc()