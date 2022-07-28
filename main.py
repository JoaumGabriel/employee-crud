import os

from tkinter import *

from buttons import MainButtons
from windows import ManyWindows
from labels import MainLabels


class MainWindow:  # Janela Principal

    def __init__(self):

        self.mainwindow = Tk()
        self.mainwindow.title("Menu Principal | Scene1")
        self.mainwindow.geometry("860x600")
        self.mainwindow.resizable(False, False)
        self.mainwindow.configure(background='gray')


def printConsole():

    print("Olá Mundo")


def closePgm():

    Janela.mainwindow.destroy()
    print("Janela fechada com sucesso!")


def createWindow():

    ManyWindows()
    
def readWindow():
    
    ManyWindows()


"""

CHAMANDO CLASSES E SEUS COMPONENTS PARA A EXECUÇÃO

"""

Janela = MainWindow()
Btn = MainButtons()
Lb = MainLabels()

Btn.closeBtn(Janela.mainwindow, closePgm)
Btn.createFuncionario(Janela.mainwindow, createWindow)
Btn.editFuncionario(Janela.mainwindow, printConsole)
Btn.readFuncionario(Janela.mainwindow, readWindow)
Lb.labelTitle(Janela.mainwindow)

Janela.mainwindow.mainloop()
