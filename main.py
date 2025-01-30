from tkinter import Tk
import os
import platform

from src.gestionbdd import GestionBdd
from interface.toplevel.toplevel_nouvelle_table import ToplevelNouvelleTable
from interface.toplevel.toplevel_nouvelle_base import ToplevelNouvelleBase
from interface.toplevel.toplevel_charger_base import ToplevelChargerBase
from interface.toplevel.toplevel_modifier_table import ToplevelModifierTable
from interface.toplevel.toplevel_delete_table import ToplevelDeleteTable


class Root(Tk):
    def __init__(self, mode_os):

        self.mode_os = mode_os
        Tk.__init__(self)
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.fenetre_nouvelle_base=None
        self.fenetre_nouvelle_table=None
        self.base_de_donnee_active=None
        self.fenetre_charger_bdd = None
        self.index_temp_modifier_table=None
        self.fenetre_modifier_table =None
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
        self.base_de_donnee_active = self.gestionbdd.open_database("data1")
        self.interface.mise_a_jour_database(self.base_de_donnee_active)

    def demande_nouvelle_base_de_donnee(self):
        self.fenetre_nouvelle_base = ToplevelNouvelleBase(self)

    def sortie_toplevel_nouvelle_base_de_donnee(self,**kwargs):
        self.base_de_donnee_active=self.gestionbdd.cree_objet_base_de_donne(**kwargs)
        self.sauvegarder_base_de_donnee()
        self.fenetre_nouvelle_base.destroy()
        self.base_de_donnee_active = self.gestionbdd.open_database(kwargs['name'])
        self.interface.mise_a_jour_database(self.base_de_donnee_active)

    def demande_nouvelle_table(self):
        self.fenetre_nouvelle_table=ToplevelNouvelleTable(self)

    def sortie_toplevel_nouvelle_table(self,**kwargs):
        self.base_de_donnee_active.add_table(kwargs['name'],kwargs["types_column"])
        self.sauvegarder_base_de_donnee()
        self.base_de_donnee_active=self.gestionbdd.open_database(self.base_de_donnee_active.name)
        self.interface.mise_a_jour_database(self.base_de_donnee_active)
        self.fenetre_nouvelle_table.destroy()

    def sauvegarder_base_de_donnee(self):
        self.gestionbdd.sauvegarder_base_de_donnee(self.base_de_donnee_active)

    def demande_charger_base_de_donnee(self):
        self.fenetre_charger_bdd=ToplevelChargerBase(self,self.path)

    def sortie_toplevel_charger_base_de_donnee(self,name):
        self.base_de_donnee_active=self.gestionbdd.open_database(name)
        self.interface.mise_a_jour_database(self.base_de_donnee_active)
        self.fenetre_charger_bdd.destroy()

    def demande_modifier_table(self,index):
        self.index_temp_modifier_table=index
        self.fenetre_modifier_table=ToplevelModifierTable(self,self.base_de_donnee_active.names_table[index],
                                                          self.base_de_donnee_active.types_column[index])

    def sortie_toplevel_modifier_table(self,**kwargs):
        self.base_de_donnee_active.delete_table(self.index_temp_modifier_table)
        self.base_de_donnee_active.add_table(kwargs["name"],kwargs['types_column'])
        self.sauvegarder_base_de_donnee()
        self.base_de_donnee_active = self.gestionbdd.open_database(self.base_de_donnee_active.name)
        self.interface.mise_a_jour_database(self.base_de_donnee_active)
        self.fenetre_modifier_table.destroy()

    def demande_delete_table(self,index):
        self.index_temp_modifier_table = index
        self.fenetre_delete_table=ToplevelDeleteTable(self,self.base_de_donnee_active.names_table[index])

    def sortie_toplevel_delete_table(self):
        self.base_de_donnee_active.delete_table(self.index_temp_modifier_table)
        self.sauvegarder_base_de_donnee()
        self.base_de_donnee_active = self.gestionbdd.open_database(self.base_de_donnee_active.name)
        self.interface.mise_a_jour_database(self.base_de_donnee_active)
        self.fenetre_delete_table.destroy()



if __name__=="__main__":
    plat_form=platform.system()
    root=Root(plat_form)
    root.mainloop()
    root.gestionbdd.close_connexion_focus()