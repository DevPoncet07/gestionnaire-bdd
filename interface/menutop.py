from tkinter import Menu



class MenuTop(Menu):
    def __init__(self,boss):
        self.boss=boss
        Menu.__init__(self,master=boss)
        menu_file=Menu(self,tearoff=0)
        menu_file.add_command(label='Nouvelle base de donnee',command=self.boss.demande_nouvelle_base)
        menu_file.add_command(label='Charger base de donnee',command=self.boss.charger_base_de_donnee)
        menu_file.add_command(label='Sauvegarder base de donnee',command=self.boss.sauvegarder_base_de_donnee)
        self.add_cascade(label='File',menu=menu_file)

        menu_table=Menu(self,tearoff=0)
        menu_table.add_command(label='Nouvelle table',command=self.boss.demande_nouvelle_table)
        menu_table.add_command(label='Modifier table',command=self.boss.demande_modifier_table)
        menu_table.add_command(label='Supprime table',command=self.boss.demande_delete_table)
        self.add_cascade(label='Table',menu=menu_table)