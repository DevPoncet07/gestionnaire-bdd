from tkinter import Toplevel,Entry,Label,StringVar,Button


class ToplevelSaveDatabase(Toplevel):
    def __init__(self,boss,filename):
        self.boss=boss
        Toplevel.__init__(self)

        Label(self,text='Are you sure to save in '+str(filename)).grid(row=0,column=0)


        Button(self,text='Valid',command=self.valid).grid(row=1,column=0,columnspan=2)

    def valid(self):
        self.boss.answer_save_object_database_into_file()