from tkinter import Frame, Canvas,Text,Entry,Label,StringVar,ALL


class InterfaceDesktop(Frame):
    def __init__(self, boss):
        self.boss = boss

        Frame.__init__(self, master=boss, bg="grey30",width=500,height=500)

        self.can = Canvas(self, width=500, height=500, bg='grey20')
        self.can.grid(row=0, column=0,padx=10,pady=10)

        self.frame_entry=Frame(self,bg='grey30')
        self.frame_entry.grid(row=0,column=1)
        self.text=Text(self.frame_entry,width=60,height=20,bg='grey20',state='disabled',fg='white')
        self.text.grid(row=0,column=0,columnspan=2)
        Label(self.frame_entry,text="Commande python : ",bg='grey30',fg='white').grid(row=1,column=0)
        self.str_entry=StringVar()
        self.entry_text=Entry(self.frame_entry,width=50,bg='grey20',fg='white',textvariable=self.str_entry,)
        self.entry_text.bind("<Return>",self.sortie_entry)
        self.entry_text.grid(row=1,column=1)


    def sortie_entry(self,event):
        text=self.str_entry.get()
        self.boss.execute_commande(text)
        self.print(text,"commande")
        self.str_entry.set("")

    def print(self,text,mode="console"):
        text = mode + " : " + text+"\n"
        self.text['state']='normal'
        self.text.insert('end',text)
        self.text['state'] = 'disabled'

    def mise_a_jour_data(self,names_colonne,data):
        self.can.delete(ALL)
        for index in range(len(names_colonne)):
            self.can.create_rectangle(5+index*100,5,100+index*100,30,outline="white")
            self.can.create_text(30+index*100,10,anchor="nw",text=names_colonne[index],fill='white')
            for element in range(len(data)):
                self.can.create_window(10+index*100,50+element*25,anchor="nw",window=EntryCell(data[element][index]))


class EntryCell(Text):
    def __init__(self,text):
        Text.__init__(self,width=10,height=1)
        self.insert('end',text)

