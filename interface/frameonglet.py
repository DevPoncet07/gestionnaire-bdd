from tkinter import Frame,Canvas,Button,Label

class FrameOnglet(Frame):
    def __init__(self,boss,**kwargs):
        self.boss=boss
        self.name=kwargs["name"]
        self.types_column=kwargs["types_column"]
        Frame.__init__(self,master=boss)
        Label(self,text='Nom de la table : '+self.name).grid(row=0,column=0)
        self.can=Canvas(self,width=500,height=500,bg='white')
        self.can.grid(row=1,column=0)
        self.create_column_info()

    def create_column_info(self):
        for index in range(len(self.types_column)):
            self.can.create_rectangle(5+100*index,5,5+100*index+100,40)
            self.can.create_text(55+100*index,15,anchor='center',text=str(self.types_column[index][1]))
            self.can.create_text(55 + 100 * index, 30, anchor='center', text=str(self.types_column[index][2]))