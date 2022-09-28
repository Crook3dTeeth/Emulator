#from turtle import*
import pyglet 


def readBus():
    pass

class Graphics:

    def __init__(self, width, height, id, pcieSlot):
        self.width = width
        self.height = height
        self.id = id
        self.pcieSlot = pcieSlot

        pass

    def createWindow(self):
        
        window = pyglet.window.Window()
        #label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
        self.window = window

    def updateWindow(self):
        pass

