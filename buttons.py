from tkinter import *
from tkinter import ttk


class MainButtons:  # Classe de botões

    def closeBtn(self, window, command):

        self.photo = PhotoImage(file="src/images/power_icon.png")

        self.photoimage3 = self.photo.subsample(2, 2)

        self.s = ttk.Style()
        self.s.configure('bt2.TButton', background='gray',
                         foreground='black', padding=(-20, 5, -20, 5), font="Helvetica, 12",
                         image=self.photoimage3)

        self.bt = ttk.Button(window, text="Sair",
                             command=command, style='bt2.TButton', compound=LEFT)
        self.bt.place(x=750, y=550)

    def createFuncionario(self, window, comando):

        self.photo = PhotoImage(file="src/images/profile_icon.png")

        self.CreatePhoto = self.photo.subsample(2, 2)

        self.s = ttk.Style()
        self.s.configure('create.TButton', background='gray',
                         image=self.CreatePhoto, font="Arial, 13",
                         padding=(5, 5, 5, 5))

        self.bt = ttk.Button(window, text=" Criar Funcionário",
                             style='create.TButton', compound=LEFT, command=comando)
        self.bt.place(x=342, y=170)

    def editFuncionario(self, window, comando):

        self.photo = PhotoImage(file="src/images/manage_profile.png")

        self.EditPhoto = self.photo.subsample(2, 2)

        self.s = ttk.Style()
        self.s.configure('edit.TButton', background='gray',
                         image=self.EditPhoto, font="Arial, 13",
                         padding=(5, 5, 5, 5))

        self.bt = ttk.Button(window, text=" Editar Funcionário",
                             style='edit.TButton', compound=LEFT, command=comando)
        self.bt.place(x=340, y=240)

    def readFuncionario(self, window, comando):

        self.photo = PhotoImage(file="src/images/read_icon.png")

        self.ReadPhoto = self.photo.subsample(2, 2)

        self.s = ttk.Style()
        self.s.configure('read.TButton', background='gray',
                         image=self.ReadPhoto, font="Arial, 13", padding=(5, 5, 5, 5))

        self.bt = ttk.Button(window, text=" Visualizar Funcionários",
                             style="read.TButton", compound=LEFT, command=comando)
        self.bt.place(x=325, y=310)
