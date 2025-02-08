from tkinter import Toplevel, Button, Entry, Label, StringVar, Frame, LabelFrame, Listbox,Text,Scrollbar

from .toplevel_new_table import ToplevelNewTable
from .toplevel_modifier_table import ToplevelModifierTable


class ToplevelNewDatabase(Toplevel):
    def __init__(self,boss):
        self.boss=boss
        self.index_table_focus=None
        self.tables_names=[]
        self.column_names=[]
        self.window_new_table=None
        self.window_modify_table=None

        Toplevel.__init__(self)

        frame_name=Frame(self)
        frame_name.grid(row=0,column=0,padx=10,pady=10)
        Label(frame_name,text="nom de la nouvelle base de donnee: ").grid(row=0,column=0)
        self.str_name_table=StringVar()
        self.entry_name=Entry(frame_name,width=30,textvariable=self.str_name_table)
        self.entry_name.grid(row=0,column=1)
        frame_tables=LabelFrame(self,text='tables')
        frame_tables.grid(row=1,column=0,padx=10,pady=10)
        Button(frame_tables,text="Nouvelle tables",command=self.ask_window_new_table).grid(row=0,column=0,padx=10,pady=10)
        Button(frame_tables, text="Modifie tables", command=self.aks_window_modify_table).grid(row=1, column=0, padx=10,
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

        Button(self, text='Valider', command=self.answer).grid(row=5, column=0)

    def remplir_listbox(self,names):
        self.listbox_table.delete(0,'end')
        for name in names:
            self.listbox_table.insert('end',name)

    def sortie_listbox_table(self,event):
        index=self.listbox_table.curselection()
        self.index_table_focus=index[0]
        self.text_column['state']='normal'
        self.text_column.delete(0.0,'end')
        for column in self.column_names[self.index_table_focus]:
            self.text_column.insert('end',str(column)+"\n")
        self.text_column['state'] = 'disabled'

    def ask_window_new_table(self):
        self.window_new_table=ToplevelNewTable(self)

    def answer_window_new_table(self,name,types_column):
        self.tables_names.append(name)
        self.column_names.append(types_column)
        self.remplir_listbox(self.tables_names)
        self.window_new_table.destroy()

    def aks_window_modify_table(self):
        self.window_modify_table=ToplevelModifierTable(self,self.tables_names[self.index_table_focus],self.column_names[self.index_table_focus])

    def answer_window_modify_table(self,table_name,column_names):
        self.delete_table()
        self.tables_names.insert(self.index_table_focus,table_name)
        self.column_names.insert(self.index_table_focus,column_names)
        self.remplir_listbox(self.tables_names)
        self.window_modify_table.destroy()

    def delete_table(self):
        del self.tables_names[self.index_table_focus]
        del self.column_names[self.index_table_focus]
        self.remplir_listbox(self.tables_names)


    def answer(self):
        name=self.str_name_table.get()
        self.boss.answer_window_new_database(filename=name, table_names=self.tables_names, column_infos=self.column_names)