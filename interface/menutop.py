from tkinter import Menu



class MenuTop(Menu):
    def __init__(self,boss):
        self.boss=boss
        Menu.__init__(self,master=boss)
        menu_file=Menu(self,tearoff=0)
        menu_file.add_command(label='Nouvelle base de donnee', command=self.boss.ask_window_new_database)
        menu_file.add_command(label='Charger base de donnee',command=self.boss.charger_base_de_donnee)
        menu_file.add_command(label='Sauvegarder base de donnee', command=self.boss.save_object_database_into_file)
        menu_file.add_command(label='Sauvegarder base de donnee as ', command=self.boss.save_object_database_into_file_as)
        self.add_cascade(label='File',menu=menu_file)

        menu_table=Menu(self,tearoff=0)
        menu_table.add_command(label='Nouvelle table', command=self.boss.ask_window_new_table)
        menu_table.add_command(label='Modifier la table actuel', command=self.boss.ask_modify_table)
        menu_table.add_command(label='Supprime la table actuel', command=self.boss.ask_delete_table)
        self.add_cascade(label='Table',menu=menu_table)