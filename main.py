from tkinter import Tk
import os
import platform

from src.gestionbdd import GestionBdd
from interface.toplevel.toplevel_new_table import ToplevelNewTable
from interface.toplevel.toplevel_new_database import ToplevelNewDatabase
from interface.toplevel.toplevel_charger_base import ToplevelChargerBase
from interface.toplevel.toplevel_modifier_table import ToplevelModifierTable
from interface.toplevel.toplevel_delete_table import ToplevelDeleteTable


class Root(Tk):
    def __init__(self, mode_os):

        self.mode_os = mode_os
        Tk.__init__(self)
        self.protocol('WN_DELETE_WINDOW',self.quit_programme_with_x)
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.windows_new_database=None
        self.window_new_table=None
        self.database_focus=None
        self.window_load_database = None
        self.index_temp_modifier_table=None
        self.window_modify_table =None
        self.fenetre_delete_table=None


        if mode_os == 'Windows':
            from interface.interfacedesktop import InterfaceDesktop
            self.interface = InterfaceDesktop(self)
            self.interface.grid(padx=10, pady=10)
        else:
            pass
            #self.interface = InterfaceTablette(self, self.path)
            #self.interface.grid()

        self.gestionbdd = GestionBdd(self, self.path)
        #self.create_database1()
        self.database_focus=self.gestionbdd.open_database_from_file('data1')
        self.interface.mise_a_jour_database(self.database_focus)

    def ask_window_new_database(self):
        self.windows_new_database = ToplevelNewDatabase(self)

    def answer_window_new_database(self, **kwargs):
        self.database_focus=self.gestionbdd.create_object_empty_database(kwargs['filename'])
        self.gestionbdd.add_multi_table_and_column_empty(self.database_focus,**kwargs)
        self.windows_new_database.destroy()
        self.interface.mise_a_jour_database(self.database_focus)

    def ask_window_new_table(self):
        self.window_new_table=ToplevelNewTable(self)

    def answer_window_new_table(self, table_names,column_names):
        self.database_focus.add_table_and_column_empty(table_names,column_names)
        self.window_new_table.destroy()
        self.interface.mise_a_jour_database(self.database_focus)

    def save_object_database_into_file(self):
        self.gestionbdd.save_object_database_into_file(self.database_focus)

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
        self.interface.mise_a_jour_database(self.database_focus)
        self.window_modify_table.destroy()

    def ask_delete_table(self,index):
        self.index_temp_modifier_table = index
        self.fenetre_delete_table=ToplevelDeleteTable(self, self.database_focus.tables_names[index])

    def answer_window_delete_table(self):
        self.database_focus.delete_table(self.index_temp_modifier_table)
        self.interface.mise_a_jour_database(self.database_focus)
        self.fenetre_delete_table.destroy()

    #########################################################################

    def demande_load_data_onglet(self,index_onglet):
        #self.database_focus=self.gestionbdd.load_data_onglet_50(self.database_focus, index_onglet)
        self.interface.mise_a_jour_datas(self.database_focus.datas_per_tables[0])

    def quit_programme_with_x(self):
        root.gestionbdd.close_connexion_focus()
        self.destroy()


    def create_database1(self):
        self.database_focus = self.gestionbdd.create_object_empty_database('data1')
        self.database_focus.add_table_and_column_empty("table_1",
                                                       [[0, "id", "INTEGER", 1, 1], [1, "nom", "TEXT", "", 0]])
        self.database_focus.add_data_one_line(0, [0, 'ad'])
        self.database_focus.add_data_one_line(0, [1, 'ad'])
        self.database_focus.add_data_one_line(0, [2, 'tt'])
        self.database_focus.add_table_and_column_empty("table_2",
                                                       [[0, "id", "INTEGER", 1, 1], [1, "nom", "TEXT", "", 0]])
        self.database_focus.add_data_one_line(1, [0, 'ad'])
        self.database_focus.add_data_one_line(1, [1, 'ad'])
        self.database_focus.add_data_one_line(1, [2, 'tt'])
        self.database_focus.add_data_one_line(1, [3, 'tt'])
        self.database_focus.add_data_one_line(1, [4, 'tt'])
        self.database_focus.add_data_one_line(1, [5, 'tt'])

        self.gestionbdd.save_object_database_into_file(self.database_focus, 'data1')



if __name__=="__main__":
    plat_form=platform.system()
    root=Root(plat_form)
    root.mainloop()
