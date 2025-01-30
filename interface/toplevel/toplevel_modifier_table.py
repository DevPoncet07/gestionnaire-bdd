from tkinter import Toplevel,Button,Entry,Label,StringVar,LabelFrame,Listbox,OptionMenu


class ToplevelModifierTable(Toplevel):
    def __init__(self,boss,name,types_column):
        self.boss=boss
        self.type_column=[]
        for element in types_column:
            self.type_column.append(element)
        self.value_type=["NULL","INTEGER","REAL","TEXT","BLOB","INTEGER PRIMARY KEY"]
        self.column_focus=-1
        Toplevel.__init__(self)

        frame_name=LabelFrame(self,text="Table")
        frame_name.grid(row=0,column=0)
        Label(frame_name,text="nom de la nouvelle table : ").grid(row=0,column=0,pady=10)
        self.str_name_table=StringVar(value=name)
        self.entry_name=Entry(frame_name,width=30,textvariable=self.str_name_table)
        self.entry_name.grid(row=0,column=1)

        frame_column=LabelFrame(self,text="Colonne")
        frame_column.grid(row=1,column=0,padx=10,pady=10)
        self.listbox_column=Listbox(frame_column,width=30,height=10)
        self.listbox_column.grid(row=0,column=0,rowspan=2,padx=10,pady=10)
        self.listbox_column.bind("<ButtonRelease-1>",self.sortie_listbox_column)

        Button(frame_column,text='Ajouter colonne',command=self.add_column).grid(row=0,column=1)

        frame_infos_column=LabelFrame(frame_column,text='Infos colonne')
        frame_infos_column.grid(row=1,column=1)
        self.str_name_column=StringVar()
        Label(frame_infos_column,text='Nom de la colonne : ').grid(row=0,column=0)
        self.entry_name_column=Entry(frame_infos_column,width=40,textvariable=self.str_name_column)
        self.entry_name_column.grid(row=0,column=1)
        self.str_type_column = StringVar(value=self.value_type[1])
        Label(frame_infos_column, text='Type de la colonne : ').grid(row=1, column=0)
        self.entry_type_column = OptionMenu(frame_infos_column,self.str_type_column,*self.value_type)
        self.entry_type_column.grid(row=1, column=1)
        self.boutton_supprimer = Button(frame_infos_column, text='Supprimer colonne',command=self.delete_column)
        self.boutton_supprimer.grid(row=2, column=0, pady=10)
        self.boutton_modifier=Button(frame_infos_column, text='Modifier colonne', command=self.modifier_column)
        self.boutton_modifier.grid(row=2,column=1,pady=10)

        Button(self,text='Modifier la table',command=self.sortie_toplevel_modifier_table).grid(row=5,column=0,pady=10)
        self.remplir_listbox(self.type_column)

    def sortie_listbox_column(self,event):
        index=self.listbox_column.curselection()
        index=index[0]
        self.column_focus=index
        self.str_name_column.set(str(self.type_column[index][1]))
        self.str_type_column.set(str(self.type_column[index][2]))


    def remplir_listbox(self,names_column):
        self.listbox_column.delete(0,'end')
        for element in names_column:
            self.listbox_column.insert('end',element[1]+" "+element[2])

    def add_column(self):
        self.type_column.append([len(self.type_column),"empty","INTEGER",0,"",0])
        self.remplir_listbox(self.type_column)
        self.column_focus = len(self.type_column)-1
        self.str_name_column.set(str(self.type_column[self.column_focus][1]))
        self.str_type_column.set("INTEGER")

    def modifier_column(self):
        if self.column_focus!=(-1):
            self.type_column[self.column_focus][1:2]=[self.str_name_column.get(),self.str_type_column.get()]
        self.remplir_listbox(self.type_column)

    def delete_column(self):
        if self.column_focus!=(-1):
            del self.type_column[self.column_focus]
        self.remplir_listbox(self.type_column)

    def sortie_toplevel_modifier_table(self):
        name=self.str_name_table.get()
        self.boss.sortie_toplevel_modifier_table(name=name,types_column=self.type_column)