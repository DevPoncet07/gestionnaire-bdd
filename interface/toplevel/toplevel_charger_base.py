from tkinter import Toplevel,Button,Label,StringVar,Listbox,LabelFrame
import os


class ToplevelChargerBase(Toplevel):
    def __init__(self,boss,path):
        self.boss=boss
        self.path=path
        self.file_names=[]
        self.index=0
        Toplevel.__init__(self)
        frame_bdd_dossier=LabelFrame(self,text='Dossier base_de_donnee')
        frame_bdd_dossier.grid(row=0,column=0)
        Label(frame_bdd_dossier,text='Base de donnee contenus dans\n le dossier local base_de_donnee').grid(row=0,column=0)
        self.listbox_projet=Listbox(frame_bdd_dossier,width=20,height=10)
        self.listbox_projet.grid(row=0,column=1)
        self.listbox_projet.bind("<ButtonRelease-1>",self.sortie_listbox_projet)

        self.remplir_listbox()

        frame_down=LabelFrame(self,text="Base de donnee selectionner",width=350,height=120)
        frame_down.grid(row=1, column=0, padx=10, pady=10)


        self.str_name_bdd = StringVar()
        self.str_name_bdd.set("nom de la base de donnee charger : ")
        Label(frame_down,textvariable=self.str_name_bdd).place(x=50,y=20)

        Button(frame_down,text='Valider',command=self.sortie_toplevel_charger_base_de_donnee).place(x=120,y=50)

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
        self.boss.answer_window_load_database(name=name)
