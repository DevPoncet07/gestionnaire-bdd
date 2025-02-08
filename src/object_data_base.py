"""
Class BaseDeDonnee est la classe de stockage des informations de la base de donnee ouverte
toutes les donnees modifier grace a l'interface sont stocké ici puis une fois que l'utilisateur
sauvegarde, le programme se sert de cette classe pour cree une base de donne .db.
"""

class ObjectDataBase:
    def __init__(self,filename):
        self.filename=filename
        self.tables_names=[]
        self.number_of_tables=0
        self.column_names=[]
        self.datas_per_tables=[]
        self.len_column_per_tables=[]

    def __str__(self):
        txt="Filename : "+str(self.filename)+"\n"
        txt+="Number of table : "+str(self.number_of_tables)+"\n"
        txt += "Table name : "
        for table in range(self.number_of_tables):
            txt+=str(self.tables_names[table])+" "
        txt+="\nTables informations : \n"
        for table in range(self.number_of_tables):
            txt+=str(self.tables_names[table])+" :"
            for infos in self.column_names[table]:
                txt+=" ["+str(infos[1])+" "+str(infos[2])+"] "
        return txt

    def add_table_empty(self,table_name):
        self.tables_names.append(table_name)
        self.column_names.append([])
        self.len_column_per_tables.append(0)
        self.number_of_tables+=1

    def add_multi_table_and_column_empty(self,table_name,column_names):
        for index in range(len(table_name)):
            self.add_table_and_column_empty(table_name[index],column_names[index])

    def add_table_and_column_empty(self,table_name,column_names):
        self.tables_names.append(table_name)
        self.column_names.append(column_names)
        self.len_column_per_tables.append(len(column_names))
        self.datas_per_tables.append([])
        self.number_of_tables+=1

    def add_data_one_line(self,table_index,data):
        self.datas_per_tables[table_index].append(data)

    def modify_table_by_index(self,index,new_table_name,new_column_names):
        self.tables_names[index]=new_table_name
        self.column_names[index]=new_column_names
        self.len_column_per_tables.append(len(new_column_names))
        self.analyse_modify_table(index)

    def analyse_modify_table(self,index):
        nb_column=len(self.column_names[index])
        for row in range(len(self.datas_per_tables[index])):
            while len(self.datas_per_tables[index][row])<nb_column:
                self.datas_per_tables[index][row].append("NULL")

    def delete_data_one_line(self,index_table,index_row):
        del self.datas_per_tables[index_table][index_row]

    def delete_table(self, index):
        del self.tables_names[index]
        del self.column_names[index]
        del self.len_column_per_tables[index]
        del self.datas_per_tables[index]
        self.number_of_tables -= 1