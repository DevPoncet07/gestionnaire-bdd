import sqlite3

class GestionBdd:
	def __init__(self,boss,path):
		self.boss=boss
		self.path=path
		self.connexion_focus=None
		self.names_table =[]
		self.name_table_focus = ""
		self.names_column_focus =[]
		self.data = []

	def create_new_database(self,name):
		self.connexion_focus=sqlite3.connect(self.path+'/base_de_donnee/'+str(name)+".db")

	def create_table(self,arg):
		cur=self.connexion_focus.cursor()
		self.names_column_focus =arg[1:]
		cur.execute("CREATE TABLE %s (%s,%s,%s)"%(arg[0],arg[1],arg[2],arg[3]))
		self.name_table_focus = arg[0]
		cur.close()


	def insert_row_into_table(self,name,arg):
		cursor = self.connexion_focus.cursor()
		text="INSERT INTO %s(name,age,sexe) VALUES("%name
		cursor.execute(text+":name,:age,:sexe)",arg)
		self.connexion_focus.commit()
		cursor.close()

	def insert_many_row_into_table(self,name,args):
		cursor = self.connexion_focus.cursor()
		text="INSERT INTO %s (name,age,sexe) VALUES(" %name
		cursor.executemany(text+":name,:age,:sexe)",args)
		self.connexion_focus.commit()
		cursor.close()


	def open_database(self, name):
		self.connexion_focus = sqlite3.connect(self.path + "/base_de_donnee/" + str(name) + ".db")
		cursor = self.connexion_focus.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
		self.names_table = cursor.fetchall()
		cursor.close()

	def close_database_focus(self):
		if self.connexion_focus is not None:
			self.connexion_focus.close()
			self.connexion_focus = None
			self.names_table = []
			self.name_table_focus=""
			self.names_column_focus = []

	def open_table(self,name):
		cursor=self.connexion_focus.cursor()
		cursor.execute('select * from %s' %name)
		self.name_table_focus=name
		self.names_column_focus=[description[0] for description in cursor.description]
		cursor.close()

	def select_command(self,command):
		cursor=self.connexion_focus.cursor()
		cursor.execute("SELECT %s FROM %s" % (command[0],command[1]))
		self.data=[]
		for ligne in cursor.fetchall():
			self.data.append(ligne)
		return self.data

