#Inicio.
from tkinter import *

window = Tk()

class application():
    def __init__(self):
        self.window = window
        self.tela()
        self.frames_da_tela()
        self.botao_es()
        window.mainloop()
    def tela(self):
        self.window.title('Ferramentas')
        self.window.configure(background = '#13bd98')
        self.window.geometry('700x500')
        self.window.resizable(True, True)
        self.window.maxsize(width = 1000, height = 600 )
        self.window.minsize(width = 500, height = 410)
    def frames_da_tela(self):
# frame_1
        self.frame_1 = Frame(self.window, bd = 4, bg = '#d3d3d3', highlightbackground = '#faf0e6', highlightthickness = 2)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.47)
# frame_2        
        self.frame_2 = Frame(self.window, bd = 4, bg = '#d3d3d3', highlightbackground = '#faf0e6', highlightthickness = 2)
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.47)
    def botao_es(self):
# botão limpar
        self.bt_limpar = Button(self.frame_1, text = 'Limpar', bd = 3, bg = '#d8a64b', fg = 'white', font = ('helvetica', 9, 'bold'))
        self.bt_limpar.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.15)
# botão buscar
        self.bt_buscar = Button(self.frame_1, text = 'Buscar')
        self.bt_buscar.place(relx = 0.3, rely = 0.1, relwidth = 0.1, relheight = 0.15)
# botão novo
        self.bt_novo = Button(self.frame_1, text = 'Novo')
        self.bt_novo.place(relx = 0.6, rely = 0.1, relwidth = 0.1, relheight = 0.15)
# botão alterar
        self.bt_alterar = Button(self.frame_1, text = 'Alterar')
        self.bt_alterar.place(relx = 0.7, rely = 0.1, relwidth = 0.1, relheight = 0.15)
# botão apagar
        self.bt_apagar = Button(self.frame_1, text = 'Apagar')
        self.bt_apagar.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.15)
# Label código
        self.lb_codigo = Label(self.frame_1, text = 'Código')
        self.lb_codigo.place(relx = 0.031, rely = 0.03)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.03, rely = 0.18, relwidth = 0.08, relheight = 0.1)
# Label nome
        self.lb_nome = Label(self.frame_1, text = 'Nome')
        self.lb_nome.place(relx = 0.031, rely = 0.33)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.03, rely = 0.479, relwidth = 0.4, relheight = 0.1)
# Label telefone
        self.lb_telefone = Label(self.frame_1, text = 'Telefone')
        self.lb_telefone.place(relx = 0.031, rely = 0.63)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx = 0.03, rely = 0.779, relwidth = 0.4, relheight = 0.1)
# Label cidade

application()
