from tkinter import Frame, Canvas, Label, ALL, Scrollbar


class FrameOnglet(Frame):
    def __init__(self,boss,**kwargs):
        self.boss=boss
        self.name=kwargs["name"]
        self.types_column=kwargs["types_column"]
        self.taille_x_case=150
        Frame.__init__(self,master=boss)
        Label(self,text='Nom de la table : '+self.name).grid(row=0,column=0)

        frame_canvas=Frame(self)
        frame_canvas.grid(row=1,column=0)
        self.can_head=Canvas(frame_canvas,width=751,height=36,bg='white',borderwidth=0,highlightthickness=0)
        self.can_head.grid(row=0,column=1,pady=5)
        self.can_index = Canvas(frame_canvas, width=36, height=501, bg='white', borderwidth=0, highlightthickness=0)
        self.can_index.grid(row=1, column=0, padx=5)
        self.can=Canvas(frame_canvas,width=751,height=501,bg='white',borderwidth=0,highlightthickness=0)
        self.can.grid(row=1,column=1)
        self.scrollbar_y=Scrollbar(frame_canvas,orient="vertical",command=self.y_view)
        self.scrollbar_y.grid(row=1,column=2,sticky='ns')
        self.scrollbar_x = Scrollbar(frame_canvas, orient="horizontal",command=self.x_view)
        self.scrollbar_x.grid(row=2, column=1, sticky='ew')
        self.can.config(xscrollcommand=self.scrollbar_x.set,yscrollcommand=self.scrollbar_y.set)
        self.can_head.config(xscrollcommand=self.scrollbar_x.set)
        self.can_index.config(yscrollcommand=self.scrollbar_y.set)
        self.create_column_info()

    def create_column_info(self):
        self.can_head.delete(ALL)
        for index in range(len(self.types_column)):
            self.can_head.create_rectangle(self.taille_x_case*index,0,self.taille_x_case*index+self.taille_x_case,35,fill='white')
            self.can_head.create_text(10+self.taille_x_case*index,12,anchor='w',text=str(self.types_column[index][1]))
            self.can_head.create_text(10 + self.taille_x_case * index, 27, anchor='w', text=str(self.types_column[index][2]))

    def mise_a_jour_datas(self,datas):
        self.create_column_info()
        self.can.delete(ALL)
        self.can_index.delete(ALL)
        taille_y=len(datas)
        taille_x=len(self.types_column)
        if datas:
            for y in range(taille_y):
                for x in range(taille_x):
                    self.can.create_rectangle( self.taille_x_case * x, 25*y,   150 * x + self.taille_x_case, 25*y+25)
                    self.can.create_text(10+self.taille_x_case*x,5+25*y,anchor='nw',text=str(datas[y][x]))
                self.can_index.create_rectangle(0,25*y,35,25*y+25)
                self.can_index.create_text(4,6+25*y,anchor='nw',text=str(datas[y][0]))
        self.can.config(scrollregion=(0,0,1+self.taille_x_case*taille_x,1+25*taille_y))
        self.can_head.config(scrollregion=(0,0,1+self.taille_x_case*taille_x,40))
        self.can_index.config(scrollregion=(0,0,35,1+25*taille_y))

    def x_view(self,*args):
        self.can.xview(args[0],args[1])
        self.can_head.xview(args[0],args[1])

    def y_view(self,*args):
        self.can.yview(args[0], args[1])
        self.can_index.yview(args[0], args[1])