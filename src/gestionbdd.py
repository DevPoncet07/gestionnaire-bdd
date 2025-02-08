import os
import sqlite3

from .object_data_base import ObjectDataBase

class GestionBdd:
	def __init__(self,boss,path):
		self.boss=boss
		self.path=path
		self.connexion_focus=None
		self.base_de_donnee_active=None

	def create_object_empty_database(self,filename):
		database = ObjectDataBase(filename)
		return database

	def save_object_database_into_file(self,database,filename=""):
		if filename=="":
			filename=database.filename
		liste_name_file=os.listdir(self.path + "/base_de_donnee/")
		liste_bdd=[]
		for e in liste_name_file:
			liste_bdd.append(e[:-3])
		if filename in liste_bdd:
			os.remove(self.path + "/base_de_donnee/"+filename+".db")
		self.connexion_focus = sqlite3.connect(self.path + "/base_de_donnee/" + str(filename) + ".db")
		cursor = self.connexion_focus.cursor()
		for index in range(len(database.tables_names)):
			table_name=database.tables_names[index]
			txt_nom_column=""
			text = "CREATE TABLE " + table_name + " ( "
			for colone in database.column_names[index]:
				text += str(colone[1]) + " " + str(colone[2]) + ", "
				txt_nom_column+=str(colone[1])+", "
			text = text[:-2] + " );"
			txt_nom_column=txt_nom_column[0:-2]
			cursor.execute(text)
			self.connexion_focus.commit()
			for data in range(len(database.datas_per_tables[index])):
				text="INSERT INTO "+str(table_name)+"( "+txt_nom_column+" ) VALUES ( "
				for element in database.datas_per_tables[index][data]:
					if type(element)==type(""):
						text+="'"+element+"', "
					else:
						text+= str(element)+", "
				text=text[0:-2]+" );"
				cursor.execute(text)
		self.connexion_focus.commit()
		cursor.close()
		self.close_connexion_focus()

	def open_database_from_file(self, filename):
		self.connexion_focus = sqlite3.connect(self.path + "/base_de_donnee/" + str(filename) + ".db")
		cursor = self.connexion_focus.cursor()
		database = ObjectDataBase(filename)
		cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
		names_table = []
		types_column=[]
		datas_per_tables=[]
		for table in cursor.fetchall():
			names_table.append(table[1])
		for element in names_table:
			txt="PRAGMA table_info ( {} ) ;".format(element)
			cursor.execute(txt)
			liste_temp_column=[]
			for e in cursor.fetchall():
				liste_temp_column.append(e)
			types_column.append(liste_temp_column)
			cursor.execute('SELECT * FROM '+element)
			datas=[]
			for data in cursor.fetchall():
				datas.append(list(data))
			datas_per_tables.append(datas)
		for index_table in range(len(names_table)):
			database.add_table_and_column_empty(names_table[index_table],types_column[index_table])
			for element in datas_per_tables[index_table]:
				database.add_data_one_line(index_table,element)
		cursor.close()
		self.close_connexion_focus()
		return database

	def close_connexion_focus(self):
		if self.connexion_focus is not None:
			self.connexion_focus.close()
			self.connexion_focus = None





