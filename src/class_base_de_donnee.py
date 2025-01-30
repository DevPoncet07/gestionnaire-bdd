

class BaseDeDonnee:
    def __init__(self,name,names_table,types_column):
        self.name=name
        self.names_table=names_table
        self.types_column=types_column

    def __str__(self):
        return str(self.name)+" "+str(self.names_table)

    def add_table(self,name,types_column):
        self.names_table.append(name)
        self.types_column.append(types_column)

    def delete_table(self, index):
        del self.names_table[index]
        del self.types_column[index]