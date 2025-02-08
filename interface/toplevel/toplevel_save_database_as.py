from tkinter import Toplevel,Entry,Label,StringVar,Button


class ToplevelSaveDatabaseAs(Toplevel):
    def __init__(self,boss):
        self.boss=boss
        Toplevel.__init__(self)

        Label(self,text='File name : ').grid(row=0,column=0)

        self.str_name=StringVar()
        self.entry_name=Entry(self,width=30,textvariable=self.str_name)
        self.entry_name.grid(row=0,column=1)

        Button(self,text='Valid',command=self.valid).grid(row=1,column=0,columnspan=2)

    def valid(self):
        name=self.str_name.get()
        self.boss.answer_save_object_database_into_file_as(name)