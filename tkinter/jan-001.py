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
        self.window.configure(background = '#0099ff')
        self.window.geometry('700x500')
        self.window.resizable(True, True)
        self.window.maxsize(width = 1000, height = 600 )
        self.window.minsize(width = 500, height = 410)
    def frames_da_tela(self):
# frame_1
        self.frame_1 = Frame(self.window, bd = 4, bg = '#d3d3d3', highlightbackground = '#faf0e6', highlightthickness = 2)
        self.frame_1.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.43)
# frame_2        
        self.frame_2 = Frame(self.window, bd = 4, bg = '#d3d3d3', highlightbackground = '#faf0e6', highlightthickness = 2)
        self.frame_2.place(relx = 0.01, rely = 0.45, relwidth = 0.98, relheight = 0.54)
    def botao_es(self):
# botão limpar
        self.bt_limpar = Button(self.frame_1, text = 'Limpar', bd = 3, bg = '#d8a64b', fg = 'white', font = ('helvetica', 9, 'bold'))
        self.bt_limpar.place(relx = 0.1, rely = 0.02, relwidth = 0.15, relheight = 0.12)
# botão buscar
        self.bt_buscar = Button(self.frame_1, text = 'Buscar', bd = 3, bg = '#d8a64b', fg = 'white', font = ('helvetica', 9, 'bold'))
        self.bt_buscar.place(relx = 0.25, rely = 0.02, relwidth = 0.15, relheight = 0.12)
# botão novo
        self.bt_novo = Button(self.frame_1, text = 'Novo', bd = 3, bg = '#d8a64b', fg = 'white', font = ('helvetica', 9, 'bold'))
        self.bt_novo.place(relx = 0.45, rely = 0.02, relwidth = 0.15, relheight = 0.12)
# botão alterar
        self.bt_alterar = Button(self.frame_1, text = 'Alterar', bd = 3, bg = '#d8a64b', fg = 'white', font = ('helvetica', 9, 'bold'))
        self.bt_alterar.place(relx = 0.6, rely = 0.02, relwidth = 0.15, relheight = 0.12)
# botão apagar
        self.bt_apagar = Button(self.frame_1, text = 'Apagar', bd = 3, bg = '#d8a64b', fg = 'white', font = ('helvetica', 9, 'bold'))
        self.bt_apagar.place(relx = 0.75, rely = 0.02, relwidth = 0.15, relheight = 0.12)
# Label código
        self.lb_codigo = Label(self.frame_1, text = 'Código', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_codigo.place(relx = 0.1, rely = 0.15)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.25, rely = 0.15, relwidth = 0.15, relheight = 0.1)
# Label nome
        self.lb_nome = Label(self.frame_1, text = 'Nome', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_nome.place(relx = 0.1, rely = 0.3)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.25, rely = 0.3, relwidth = 0.65, relheight = 0.1)
# Label marca
        self.lb_marca = Label(self.frame_1, text = 'Marca', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_marca.place(relx = 0.1, rely = 0.45)

        self.marca_entry = Entry(self.frame_1)
        self.marca_entry.place(relx = 0.25, rely = 0.45, relwidth = 0.2, relheight = 0.1)
# Label calibragem
        self.lb_calibragem = Label(self.frame_1, text = 'Calibragem', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_calibragem.place(relx = 0.55, rely = 0.45)

        self.calibragem_entry = Entry(self.frame_1)
        self.calibragem_entry.place(relx = 0.70, rely = 0.45, relwidth = 0.2, relheight = 0.1)
# Label quantidade
        self.lb_quantidade = Label(self.frame_1, text = 'Quantidade', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_quantidade.place(relx = 0.1, rely = 0.6)

        self.quantidade_entry = Entry(self.frame_1)
        self.quantidade_entry.place(relx = 0.25, rely = 0.6, relwidth = 0.2, relheight = 0.1)
# Label valor
        self.lb_valor = Label(self.frame_1, text = 'Valor', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_valor.place(relx = 0.55, rely = 0.6)

        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx = 0.7, rely = 0.6, relwidth = 0.2, relheight = 0.1)
# Label data de aquisição
        self.lb_data_compra = Label(self.frame_1, text = 'Data-Entrada', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_data_compra.place(relx = 0.1, rely = 0.75)

        self.data_compra_entry = Entry(self.frame_1)
        self.data_compra_entry.place(relx = 0.25, rely = 0.75, relwidth = 0.2, relheight = 0.1)
# Label data de baixa
        self.lb_baixa = Label(self.frame_1, text = 'Baixa', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_baixa.place(relx = 0.55, rely = 0.75)

        self.data_baixa_entry = Entry(self.frame_1)
        self.data_baixa_entry.place(relx = 0.70, rely = 0.75, relwidth = 0.2, relheight = 0.1)
# Comentários
        self.lb_comentario = Label(self.frame_1, text = 'Comentarios', bg = '#d3d3d3', fg = '#0099ff')
        self.lb_comentario.place(relx = 0.1, rely = 0.90)

        self.comentario_entry = Entry(self.frame_1)
        self.comentario_entry.place(relx = 0.25, rely = 0.90, relwidth = 0.65, relheight = 0.1)

application()
