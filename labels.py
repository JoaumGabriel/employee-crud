from tkinter import *
from tkinter import ttk

class MainLabels:  # Classe de Textos / Labels

    def labelTitle(self, window):

        self.s = ttk.Style()
        self.s.configure('TLabel', background='gray',
                         foreground='white', font="Helvetica, 19")

        self.titulo = ttk.Label(
            window, text="Gerenciamento de Funcionários", style='TLabel')
        self.titulo.place(x=260, y=45)