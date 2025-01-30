from tkinter import Toplevel, Button, Entry, Label, StringVar, Frame, LabelFrame, Listbox,Text,Scrollbar

from .toplevel_nouvelle_table import ToplevelNouvelleTable


class ToplevelNouvelleBase(Toplevel):
    def __init__(self,boss):
        self.boss=boss
        self.index_table_focus=None
        self.names_table=[]
        self.types_column=[]
        self.fenetre_nouvelle_table=None

        Toplevel.__init__(self)

        frame_name=Frame(self)
        frame_name.grid(row=0,column=0,padx=10,pady=10)
        Label(frame_name,text="nom de la nouvelle base de donnee: ").grid(row=0,column=0)
        self.str_name_table=StringVar()
        self.entry_name=Entry(frame_name,width=30,textvariable=self.str_name_table)
        self.entry_name.grid(row=0,column=1)
        frame_tables=LabelFrame(self,text='tables')
        frame_tables.grid(row=1,column=0,padx=10,pady=10)
        Button(frame_tables,text="Nouvelle tables",command=self.demande_add_table).grid(row=0,column=0,padx=10,pady=10)
        Button(frame_tables, text="Modifie tables", command=self.demande_modifier_table).grid(row=1, column=0, padx=10,
                                                                                          pady=10)
        Button(frame_tables,text="Supprimer table",command=self.delete_table).grid(row=2,column=0,pady=10)
        self.listbox_table=Listbox(frame_tables,width=20,height=5)
        self.listbox_table.grid(row=0,column=1,rowspan=2)
        self.listbox_table.bind("<ButtonRelease-1>",self.sortie_listbox_table)

        frame_column=LabelFrame(frame_tables,text='Colonnes')
        frame_column.grid(row=0,column=2,rowspan=3,padx=15,pady=10)
        self.text_column=Text(frame_column,width=40,height=10,state='disabled')
        self.text_column.grid(row=0,column=0)
        self.scrollbar_y=Scrollbar(frame_column,orient='vertical',command=self.text_column.yview)
        self.scrollbar_y.grid(row=0,column=1,sticky='ns')

        Button(self,text='Valider',command=self.sortie_toplevel_nouvelle_base_de_donnee).grid(row=5,column=0)

    def remplir_listbox(self,names):
        self.listbox_table.delete(0,'end')
        for name in names:
            self.listbox_table.insert('end',name)

    def sortie_listbox_table(self,event):
        index=self.listbox_table.curselection()
        self.index_table_focus=index[0]
        self.text_column['state']='normal'
        self.text_column.delete(0.0,'end')
        for column in self.types_column[self.index_table_focus]:
            self.text_column.insert('end',str(column)+"\n")
        self.text_column['state'] = 'disabled'

    def demande_add_table(self):
        self.fenetre_nouvelle_table=ToplevelNouvelleTable(self)

    def sortie_toplevel_nouvelle_table(self,name,types_column):
        self.names_table.append(name)
        self.types_column.append(types_column)
        self.remplir_listbox(self.names_table)
        self.fenetre_nouvelle_table.destroy()

    def demande_modifier_table(self):
        pass

    def delete_table(self):
        pass


    def sortie_toplevel_nouvelle_base_de_donnee(self):
        name=self.str_name_table.get()
        self.boss.sortie_toplevel_nouvelle_base_de_donnee(name=name,names_table=self.names_table,types_column=self.types_column)