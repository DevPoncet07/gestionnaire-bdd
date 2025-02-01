

class BaseDeDonnee:
    def __init__(self,name,names_table,types_column):
        self.name=name
        self.names_table=names_table
        self.types_column=types_column
        self.datas=[]
        self.index_per_table=[0 for x in range(len(names_table))]

    def __str__(self):
        txt="Name : "+str(self.name)+("\n\n"
        "Table  : \n")
        for e in range(len(self.names_table)):
            txt+="          "+str(self.names_table[e])+" \n"
            for element in self.types_column[e]:
                txt+="          "+str(element)+"\n"
            txt+="\n"

        return txt

    def add_table(self,name,types_column):
        self.names_table.append(name)
        self.types_column.append(types_column)
        self.index_per_table.append(0)
        print(self.index_per_table)

    def delete_table(self, index):
        del self.names_table[index]
        del self.types_column[index]
        del self.index_per_table[index]