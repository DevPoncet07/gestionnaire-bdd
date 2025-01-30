from tkinter import Toplevel,Button,Label,StringVar,Listbox,Frame
import os


class ToplevelChargerBase(Toplevel):
    def __init__(self,boss,path):
        self.boss=boss
        self.path=path
        self.file_names=[]
        self.index=0
        Toplevel.__init__(self)

        self.listbox_projet=Listbox(self,width=20,height=10)
        self.listbox_projet.grid(row=0,column=0)
        self.listbox_projet.bind("<ButtonRelease-1>",self.sortie_listbox_projet)

        self.remplir_listbox()

        frame_down=Frame(self)
        frame_down.grid(row=1,column=0)
        self.str_name_bdd = StringVar()
        self.str_name_bdd.set("nom de la base de donnee charger : ")
        Label(frame_down,textvariable=self.str_name_bdd).grid(row=0,column=0)

        Button(frame_down,text='Valider',command=self.sortie_toplevel_charger_base_de_donnee).grid(row=1,column=0)

    def remplir_listbox(self):
        self.file_names=[]
        for name in os.listdir(self.path+'/base_de_donnee'):
            self.file_names.append(name[:-3])
        self.listbox_projet.delete(0,'end')
        for name in self.file_names:
            self.listbox_projet.insert('end',name)

    def sortie_listbox_projet(self,event):
        index=self.listbox_projet.curselection()
        self.index=index[0]
        self.str_name_bdd.set("nom de la base de donnee charger : "+str(self.file_names[self.index]))

    def sortie_toplevel_charger_base_de_donnee(self):
        name=self.file_names[self.index]
        self.boss.sortie_toplevel_charger_base_de_donnee(name=name)
