import sqlite3
import os

from .class_base_de_donnee import BaseDeDonnee

class GestionBdd:
	def __init__(self,boss,path):
		self.boss=boss
		self.path=path
		self.connexion_focus=None
		self.base_de_donnee_active=None

	def open_database(self, name):
		self.connexion_focus = sqlite3.connect(self.path + "/base_de_donnee/" + str(name) + ".db")
		cursor = self.connexion_focus.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
		names_table = []
		types_column=[]
		for table in cursor.fetchall():
			names_table.append(table[0])
		for element in names_table:
			cursor.execute("PRAGMA table_info({});".format(element))
			liste_temp_column=[]
			for e in cursor.fetchall():
				liste_temp_column.append(e)
			types_column.append(liste_temp_column)
		self.base_de_donnee_active = BaseDeDonnee(name,names_table,types_column)
		cursor.close()
		self.close_connexion_focus()
		return self.base_de_donnee_active

	def sauvegarder_base_de_donnee(self,base_de_donnee):
		self.close_connexion_focus()
		if base_de_donnee.name + ".db" in os.listdir(str(self.path) + "/base_de_donnee/"):
			os.remove(str(self.path )+ "/base_de_donnee/"+base_de_donnee.name+".db")
		self.create_data_base_and_table(base_de_donnee)

	def cree_objet_base_de_donne(self,**kwargs):
		bdd=BaseDeDonnee(**kwargs)
		return bdd

	def create_data_base_and_table(self,base_de_donnee):
		self.connexion_focus = sqlite3.connect(self.path + "/base_de_donnee/" + str(base_de_donnee.name) + ".db")
		cursor = self.connexion_focus.cursor()
		print(base_de_donnee.types_column)
		for index in range(len(base_de_donnee.names_table)):
			text="CREATE TABLE "+base_de_donnee.names_table[index]+" ( "
			for colone in base_de_donnee.types_column[index]:
				text+=str(colone[1])+" "+str(colone[2])+", "
			text=text[:-2]+str(" )")
			print("execute : ",text)
			cursor.execute(text)
		cursor.close()
		self.close_connexion_focus()

	def close_connexion_focus(self):
		if self.connexion_focus is not None:
			self.connexion_focus.close()
			self.connexion_focus = None




