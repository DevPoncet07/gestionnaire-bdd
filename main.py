from tkinter import Tk
import os
import platform
from tkinter import messagebox

from src.gestionbdd import GestionBdd
from interface.toplevel.toplevel_new_table import ToplevelNewTable
from interface.toplevel.toplevel_new_database import ToplevelNewDatabase
from interface.toplevel.toplevel_charger_base import ToplevelChargerBase
from interface.toplevel.toplevel_modifier_table import ToplevelModifierTable
from interface.toplevel.toplevel_delete_table import ToplevelDeleteTable
from interface.toplevel.toplevel_save_database_as import ToplevelSaveDatabaseAs
from interface.toplevel.toplevel_save_database import ToplevelSaveDatabase


class Root(Tk):
    def __init__(self, mode_os):

        self.mode_os = mode_os
        Tk.__init__(self)
        self.protocol('WN_DELETE_WINDOW',self.quit_programme_with_x)
        self.geometry("+0+0")
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.windows_new_database=None
        self.window_new_table=None
        self.database_focus=None
        self.window_load_database = None
        self.index_temp_modifier_table=None
        self.window_modify_table =None
        self.fenetre_delete_table=None
        self.window_save_database_as=None
        self.index_onglet_focus=None
        self.index_row_focus = None
        self.window_save_database=None


        if mode_os == 'Windows':
            from interface.interfacedesktop import InterfaceDesktop
            self.interface = InterfaceDesktop(self)
            self.interface.grid(padx=10, pady=10)
        else:
            pass
            #self.interface = InterfaceTablette(self, self.path)
            #self.interface.grid()

        self.gestionbdd = GestionBdd(self, self.path)
        self.database_focus=self.gestionbdd.open_database_from_file('data1')
        self.interface.mise_a_jour_database(self.database_focus)

    def ask_window_new_database(self):
        self.windows_new_database = ToplevelNewDatabase(self)

    def answer_window_new_database(self, filename,table_names,column_infos):
        self.database_focus=self.gestionbdd.create_object_empty_database(filename)
        self.database_focus.add_multi_table_and_column_empty(table_names,column_infos)
        self.windows_new_database.destroy()
        self.interface.mise_a_jour_database(self.database_focus)

    def ask_window_new_table(self):
        self.window_new_table=ToplevelNewTable(self)

    def answer_window_new_table(self, table_names,column_names):
        self.database_focus.add_table_and_column_empty(table_names,column_names)
        self.window_new_table.destroy()
        self.interface.mise_a_jour_database(self.database_focus)

    def save_object_database_into_file(self):
        self.window_save_database=ToplevelSaveDatabase(self,self.database_focus.filename)

    def answer_save_object_database_into_file(self):
        self.window_save_database.destroy()
        self.gestionbdd.save_object_database_into_file(self.database_focus)
        messagebox.showinfo("Save complete", "Complete")


    def save_object_database_into_file_as(self):
        self.window_save_database_as=ToplevelSaveDatabaseAs(self)

    def answer_save_object_database_into_file_as(self,filename):
        self.database_focus.filename=filename
        self.gestionbdd.save_object_database_into_file(self.database_focus)
        self.interface.mise_a_jour_table(self.database_focus,self.index_onglet_focus)
        self.window_save_database_as.destroy()

    def ask_load_database(self):
        self.window_load_database=ToplevelChargerBase(self, self.path)

    def answer_window_load_database(self, filename):
        self.database_focus=self.gestionbdd.open_database_from_file(filename)
        self.interface.mise_a_jour_database(self.database_focus)
        self.window_load_database.destroy()

    def ask_modify_table(self,index):
        self.index_temp_modifier_table=index
        self.window_modify_table=ToplevelModifierTable(self, self.database_focus.tables_names[index],
                                                       self.database_focus.column_names[index])

    def answer_window_modify_table(self,table_name,column_names):
        self.database_focus.modify_table_by_index(self.index_temp_modifier_table,table_name,column_names)
        self.interface.mise_a_jour_table(self.database_focus,self.index_onglet_focus)
        self.window_modify_table.destroy()

    def ask_delete_table(self,index):
        self.index_temp_modifier_table = index
        self.fenetre_delete_table=ToplevelDeleteTable(self, self.database_focus.tables_names[index])

    def answer_window_delete_table(self):
        self.database_focus.delete_table(self.index_temp_modifier_table)
        self.interface.mise_a_jour_database(self.database_focus)
        self.fenetre_delete_table.destroy()

    def demande_load_data_onglet(self,index_onglet,index):
        self.index_onglet_focus=index_onglet
        #self.database_focus=self.gestionbdd.load_data_onglet_50(self.database_focus, index_onglet)
        self.interface.mise_a_jour_table(self.database_focus,self.index_onglet_focus)

    def change_row_focus(self,index):
        if index<len(self.database_focus.datas_per_tables[self.index_onglet_focus]):
            self.index_row_focus=index
            self.interface.mise_a_jour_row_focus(index,self.database_focus.datas_per_tables[self.index_onglet_focus][index])

    def change_data_row_focus(self,row_data):
        for index in range(len(row_data)):
            self.database_focus.datas_per_tables[self.index_onglet_focus][self.index_row_focus][index]=row_data[index]
        self.interface.mise_a_jour_table(self.database_focus,self.index_onglet_focus)

    def add_new_row_to_table(self,data):
        self.database_focus.add_data_one_line(self.index_onglet_focus,data)
        self.interface.mise_a_jour_table(self.database_focus,self.index_onglet_focus)

    def delete_row_to_table(self):
        self.database_focus.delete_data_one_line(self.index_onglet_focus,self.index_row_focus)
        self.interface.mise_a_jour_table(self.database_focus, self.index_onglet_focus)

    def ask_next_view(self):
        self.interface.mise_a_jour_table(self.database_focus, self.index_onglet_focus,1)

    def ask_previous_view(self):
        self.interface.mise_a_jour_table(self.database_focus, self.index_onglet_focus,-1)

    def quit_programme_with_x(self):
        root.gestionbdd.close_connexion_focus()
        self.destroy()

if __name__=="__main__":
    plat_form=platform.system()
    root=Root(plat_form)
    root.mainloop()
