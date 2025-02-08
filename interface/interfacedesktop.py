from tkinter import Frame, Label, StringVar
from tkinter import ttk

from .frameonglet import FrameOnglet
from .menutop import MenuTop


class InterfaceDesktop(Frame):
    def __init__(self, boss):
        self.boss = boss
        Frame.__init__(self, master=boss,width=500,height=500)
        self.menu=MenuTop(self)
        self.boss['menu'] = self.menu

        self.str_name_base_de_donnee=StringVar()
        self.str_name_base_de_donnee.set("Nom de la base de donnee : ")
        self.label_name_base_de_donnee=Label(self,textvariable=self.str_name_base_de_donnee)
        self.label_name_base_de_donnee.grid(row=0,column=0,columnspan=2)

        self.notebook=ttk.Notebook(self)
        self.notebook.grid(row=1,column=1)
        self.notebook.bind("<<NotebookTabChanged>>", self.on_table_change)
        self.onglets = []
        self.index_onglet_actif=0

    def ask_window_new_database(self):
        self.boss.ask_window_new_database()

    def ask_window_new_table(self):
        self.boss.ask_window_new_table()

    def charger_base_de_donnee(self):
        self.boss.ask_load_database()

    def save_object_database_into_file(self):
        self.boss.save_object_database_into_file()

    def save_object_database_into_file_as(self):
        self.boss.save_object_database_into_file_as()

    def ask_modify_table(self):
        index=self.notebook.select()
        index=self.notebook.index(index)
        self.boss.ask_modify_table(index)

    def ask_delete_table(self):
        index = self.notebook.select()
        index = self.notebook.index(index)
        self.boss.ask_delete_table(index)

    def mise_a_jour_database(self,base_de_donnee):
        self.str_name_base_de_donnee.set("Nom de la base de donnee : "+str(base_de_donnee.filename))
        for element in self.onglets:
            self.notebook.forget(element)
        self.onglets=[]
        for index in range(len(base_de_donnee.tables_names)):
            self.add_onglet(name=base_de_donnee.tables_names[index], types_column=base_de_donnee.column_names[index])

    def add_onglet(self,**kwargs):
        onglet=FrameOnglet(self,**kwargs)
        self.onglets.append(onglet)
        self.notebook.add(onglet, text=onglet.name)

    def on_table_change(self,event):
        index = self.notebook.select()
        self.index_onglet_actif = self.notebook.index(index)
        self.boss.demande_load_data_onglet(self.index_onglet_actif,index)

    def mise_a_jour_datas(self,datas):
        self.onglets[self.index_onglet_actif].mise_a_jour_datas(datas)

    def change_row_focus(self,index):
        self.boss.change_row_focus(index)

    def mise_a_jour_row_focus(self,index,row_data):
        self.onglets[self.index_onglet_actif].mise_a_jour_row_focus(index,row_data)

    def change_data_row_focus(self,row_data):
        self.boss.change_data_row_focus(row_data)

    def mise_a_jour_table(self,database,index_table,step=0):
        self.onglets[index_table].types_column=database.column_names[index_table]
        self.onglets[index_table].mise_a_jour_datas(database.datas_per_tables[index_table],step)

    def add_new_row_to_table(self,data):
        self.boss.add_new_row_to_table(data)

    def delete_row_to_table(self):
        self.boss.delete_row_to_table()

    def ask_next_view(self):
        self.boss.ask_next_view()
    def ask_previous_view(self):
        self.boss.ask_previous_view()


