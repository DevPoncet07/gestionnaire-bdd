from tkinter import Tk
import os
import platform

from src.gestionbdd import GestionBdd

class Root(Tk):
	def __init__(self,mode_os):
		self.mode_os=mode_os
		Tk.__init__(self)
		self['bg']="grey30"
		self.path = os.path.dirname(os.path.realpath(__file__))
		

		if mode_os=='Windows':
			from interface.interfacedesktop import InterfaceDesktop
			self.interface = InterfaceDesktop(self)
			self.interface.grid(padx=10,pady=10)
		else:
			from interface.interfacetablette import InterfaceTablette
			self.interface = InterfaceTablette(self)
			self.interface.grid()
			
		self.gestionbdd=GestionBdd(self,self.path)

		#self.gestionbdd.create_new_database("data1")
		#self.gestionbdd.create_table(["table1","name","age","sexe"])
		#print(self.gestionbdd.names_column_focus)
		#arg=self.create_arg()
		#self.gestionbdd.insert_many_row_into_table("table1",arg)
		#self.gestionbdd.close_database_focus()

		self.gestionbdd.open_database('data1')
		self.name_bdd=self.gestionbdd.names_table[0][0]
		self.gestionbdd.open_table(self.name_bdd)
		self.names_colonne=self.gestionbdd.names_column_focus
		data=self.gestionbdd.select_command(["*","table1"])

		#self.gestionbdd.close_database_focus()

		self.interface.mise_a_jour_data(self.names_colonne,data)

	def execute_commande(self,commande):
		if commande=="print":
			print(self.gestionbdd.select_command(["*", "table1"]))
		elif commande=="close":
			self.gestionbdd.close_database_focus()
		elif "add row" in commande:
			commande=commande[7:].split()
			self.gestionbdd.insert_row_into_table(self.gestionbdd.name_table_focus,commande)
			data = self.gestionbdd.select_command(["*", "table1"])
			self.interface.mise_a_jour_data(self.names_colonne, data)
		else:
			try:
				print(commande)
				exec(commande)
			except:
				print("commande pourrit")

		
	def create_arg(self):
		arg = [
			{"name": "aaaaa", "age": 30, "sexe": "h"},
			{"name": "bbbbb", "age": 40, "sexe": "h"}
			, {"name": "ccccc", "age": 50, "sexe": "f"}
		]
		return arg

if __name__=="__main__":
	plat_form=platform.system()
	root=Root(plat_form)
	root.mainloop()
	root.gestionbdd.close_database_focus()

