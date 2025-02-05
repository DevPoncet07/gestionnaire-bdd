from tkinter import Toplevel,Button,Label



class ToplevelDeleteTable(Toplevel):
    def __init__(self,boss,name):
        self.boss=boss
        Toplevel.__init__(self)

        Label(self,text='Etes vous sure de vouloir supprimer définitivement\n la table : '+str(name)).grid(row=0,column=0,padx=30,pady=30,columnspan=2)

        Button(self,text='Valider',command=self.boss.answer_window_delete_table).grid(row=1,column=0,pady=20)
        Button(self,text='Annuler',command=self.destroy).grid(row=1,column=1)


