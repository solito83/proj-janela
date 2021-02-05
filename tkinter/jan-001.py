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
        self.window.configure(background = '#b0e0e6')
        self.window.geometry('600x360')
        self.window.resizable(True, True)
        self.window.maxsize(width = 900, height = 600 )
        self.window.minsize(width = 400, height = 360)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.window, bd = 4, bg = '#d3d3d3', highlightbackground = '#faf0e6', highlightthickness = 2)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.47)
        
        self.frame_2 = Frame(self.window, bd = 4, bg = '#d3d3d3', highlightbackground = '#faf0e6', highlightthickness = 2)
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.47)

application()
