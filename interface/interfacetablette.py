from tkinter import Frame, Label, StringVar
from tkinter import ttk
import os

from .frameonglet import FrameOnglet
from .menutop import MenuTop


class InterfaceTablette(Frame):
    def __init__(self, boss):
        self.boss = boss
        Frame.__init__(self, master=boss,width=500,height=500)
        self.menu=MenuTop(self)

        self.framebouttonleft = FrameBouttonLeft(self)
        self.framebouttonleft.grid(row=1, column=0)

        self.str_name_base_de_donnee = StringVar()
        self.str_name_base_de_donnee.set("Nom de la base de donnee : ")
        self.label_name_base_de_donnee = Label(self, textvariable=self.str_name_base_de_donnee)
        self.label_name_base_de_donnee.grid(row=0, column=0, columnspan=2)

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=1)
        self.onglets = []

    def demande_nouvelle_base(self):
        self.boss.demande_nouvelle_base_de_donnee()

    def demande_nouvelle_table(self):
        self.boss.demande_nouvelle_table()

    def charger_base_de_donnee(self):
        self.boss.demande_charger_base_de_donnee()

    def sauvegarder_base_de_donnee(self):
        self.boss.sauvegarder_base_de_donnee()

    def demande_modifier_table(self):
        index = self.notebook.select()
        index = self.notebook.index(index)
        self.boss.demande_modifier_table(index)

    def demande_delete_table(self):
        index = self.notebook.select()
        index = self.notebook.index(index)
        self.boss.demande_delete_table(index)

    def mise_a_jour_database(self, base_de_donnee):
        self.str_name_base_de_donnee.set("Nom de la base de donnee : " + str(base_de_donnee.name))
        for element in self.onglets:
            element.destroy()
        for index in range(len(base_de_donnee.names_table)):
            self.add_onglet(name=base_de_donnee.names_table[index], types_column=base_de_donnee.types_column[index])

    def add_onglet(self, **kwargs):
        onglet = FrameOnglet(self, **kwargs)
        self.onglets.append(onglet)
        self.notebook.add(onglet, text=onglet.name)



class FrameBouttonLeft(Frame):
    def __init__(self, boss):
        self.boss = boss
        Frame.__init__(self)


