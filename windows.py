from tkinter import *

class ManyWindows: # Classe dos TopLevels

    def __init__(self):

        self.ScreenCreation = Toplevel()
        self.ScreenCreation.title("CreateWindow")
        self.ScreenCreation.geometry("300x200")

        print("Abriu janela de criação")