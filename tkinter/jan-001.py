#Inicio.
from tkinter import *

window = Tk()

class application():
    def __init__(self):
        self.window = window
        self.tela()
        self.frames_da_tela()
        window.mainloop()
    def tela(self):
        self.window.title('Ferramentas')
        self.window.configure(background = 'red')
        self.window.geometry('600x360')
        self.window.resizable(True, True)
        self.window.maxsize(width = 900, height = 600 )
        self.window.minsize(width = 400, height = 360)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.window)

application()
