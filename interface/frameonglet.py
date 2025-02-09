from tkinter import Frame, Canvas, Label, ALL, Scrollbar,Text,Button,StringVar


class FrameOnglet(Frame):
    def __init__(self,boss,**kwargs):
        self.number_row = None
        self.boss=boss
        self.name=kwargs["name"]
        self.types_column=kwargs["types_column"]
        self.taille_x_case=150
        self.step_view=50
        self.view_max=0
        self.view_min=0
        self.index_row_focus=0
        self.img_row_focus=None
        self.text_img_row_focus=None
        self.liste_text_row=[]

        Frame.__init__(self,master=boss)
        frame_up=Frame(self)
        frame_up.grid(row=0,column=0)
        Label(frame_up,text='Nom de la table : '+self.name).grid(row=0,column=0,columnspan=2)
        self.str_number_row=StringVar()
        self.label_number_row=Label(frame_up,textvariable=self.str_number_row)
        self.label_number_row.grid(row=1,column=1)

        frame_part_view=Frame(frame_up)
        frame_part_view.grid(row=1,column=0,padx=20)
        self.boutton_Previous=Button(frame_part_view,text='Previous',command=self.boss.ask_previous_view)
        self.boutton_Previous.grid(row=0,column=0)
        self.str_indice_view=StringVar()
        self.label_indice_view=Label(frame_part_view,textvariable=self.str_indice_view)
        self.label_indice_view.grid(row=0,column=1,padx=20)
        self.boutton_next = Button(frame_part_view, text='Next',command=self.boss.ask_next_view)
        self.boutton_next.grid(row=0, column=2)


        frame_canvas=Frame(self)
        frame_canvas.grid(row=1,column=0)
        self.can_head=Canvas(frame_canvas,width=751,height=36,bg='white',borderwidth=0,highlightthickness=0)
        self.can_head.grid(row=0,column=1,pady=5)
        self.can_index = Canvas(frame_canvas, width=50, height=501, bg='white', borderwidth=0, highlightthickness=0)
        self.can_index.grid(row=1, column=0, padx=5)
        self.can_index.bind('<ButtonRelease-1>',self.exit_can_index)
        self.can=Canvas(frame_canvas,width=751,height=501,bg='white',borderwidth=0,highlightthickness=0)
        self.can.grid(row=1,column=1)
        self.scrollbar_y=Scrollbar(frame_canvas,orient="vertical",command=self.y_view)
        self.scrollbar_y.grid(row=1,column=2,sticky='ns')
        self.scrollbar_x = Scrollbar(frame_canvas, orient="horizontal",command=self.x_view)
        self.scrollbar_x.grid(row=2, column=1, sticky='ew')
        self.can.config(xscrollcommand=self.scrollbar_x.set,yscrollcommand=self.scrollbar_y.set)
        self.can_head.config(xscrollcommand=self.scrollbar_x.set)
        self.can_index.config(yscrollcommand=self.scrollbar_y.set)
        self.canvas_modif_row=Canvas(frame_canvas,width=751,height=60,bg='white',borderwidth=0,highlightthickness=0,xscrollcommand=self.scrollbar_x.set)
        self.canvas_modif_row.grid(row=3,column=1)

        frame_bottom=Frame(self)
        frame_bottom.grid(row=2,column=0)
        Button(frame_bottom, text="New row", command=self.new_row).grid(row=0, column=0)
        Button(frame_bottom, text="Valid change", command=self.valid_modify_row).grid(row=0, column=1,padx=20)
        Button(frame_bottom, text="Delete row", command=self.delete_row).grid(row=0, column=2)

        self.create_column_info()

    def create_column_info(self):
        self.can_head.delete(ALL)
        self.canvas_modif_row.delete(ALL)
        for index in range(len(self.types_column)):
            self.can_head.create_rectangle(self.taille_x_case*index,0,self.taille_x_case*index+self.taille_x_case,35,fill='white')
            self.can_head.create_text(10+self.taille_x_case*index,12,anchor='w',text=str(self.types_column[index][1]))
            self.can_head.create_text(10 + self.taille_x_case * index, 27, anchor='w', text=str(self.types_column[index][2]))
            self.canvas_modif_row.create_rectangle(self.taille_x_case * index, 0,
                                                   self.taille_x_case * index + self.taille_x_case, 50, fill='white')
            self.liste_text_row.append(Text(self.canvas_modif_row, width=15, height=2))
            self.canvas_modif_row.create_window(5 + self.taille_x_case * index, 5, anchor='nw',
                                                window=self.liste_text_row[-1])

    def mise_a_jour_datas(self,datas,step=0):
        self.liste_text_row=[]
        self.create_column_info()
        self.can.delete(ALL)
        self.can_index.delete(ALL)
        taille_y=len(datas)
        taille_x=len(self.types_column)
        self.number_row=taille_y
        self.adapt_view(step)
        self.str_number_row.set("Number of row : "+str(taille_y))
        self.str_indice_view.set("row : "+str(self.view_min)+" to " + str(self.view_max)+" (step "+str(self.step_view)+" )")
        if datas:
            for y in range(self.view_min,self.view_max):
                for x in range(taille_x):
                    y_temp=y-self.view_min
                    self.can.create_rectangle( self.taille_x_case * x, 25*y_temp,   150 * x + self.taille_x_case, 25*y_temp+25)
                    self.can.create_text(10+self.taille_x_case*x,5+25*y_temp,anchor='nw',text=str(datas[y][x]))
                self.can_index.create_rectangle(0,25*y_temp,35,25*y_temp+25)
                self.can_index.create_text(4,6+25*y_temp,anchor='nw',text=str(y))
        taille_y=self.view_max-self.view_min
        self.can.config(scrollregion=(0,0,1+self.taille_x_case*taille_x,1+25*taille_y))
        self.can_head.config(scrollregion=(0,0,1+self.taille_x_case*taille_x,40))
        self.can_index.config(scrollregion=(0,0,35,1+25*taille_y))
        self.canvas_modif_row.config(scrollregion=(0, 0, 1 + self.taille_x_case * taille_x, 50))

    def adapt_view(self,step):
        if self.view_min+step*self.step_view<0:
            pass
        else:
            if self.view_min + step * self.step_view>=self.number_row:
                self.view_max = self.number_row
            else:
                self.view_min += step * self.step_view
                self.view_max = self.view_min+self.step_view
        if self.view_max>self.number_row:
            self.view_max = self.number_row

    def x_view(self,*args):
        self.can.xview(args[0],args[1])
        self.can_head.xview(args[0],args[1])
        self.canvas_modif_row.xview(args[0],args[1])

    def y_view(self,*args):
        self.can.yview(args[0], args[1])
        self.can_index.yview(args[0], args[1])

    def exit_can_index(self,event):
        y=((int(self.can_index.canvasy(0))+event.y)//25)+self.view_min
        self.boss.change_row_focus(y)

    def mise_a_jour_row_focus(self,index,row_data):
        if self.img_row_focus:
            self.can_index.delete(self.img_row_focus)
            self.can_index.delete(self.text_img_row_focus)
        self.index_row_focus=index
        index-=self.view_min
        self.img_row_focus=self.can_index.create_rectangle(0, 25 * index, 35, 25 * index + 25,fill='grey80')
        self.text_img_row_focus=self.can_index.create_text(4, 6 + 25 * index, anchor='nw', text=str(self.index_row_focus))
        self.canvas_modif_row.delete(ALL)
        self.liste_text_row=[]
        for element in range(len(row_data)):
            self.canvas_modif_row.create_rectangle(self.taille_x_case * element, 0,
                                           self.taille_x_case * element + self.taille_x_case, 50, fill='white')
            self.liste_text_row.append(Text(self.canvas_modif_row, width=15, height=2))
            self.liste_text_row[-1].insert('end',str(row_data[element]))
            self.canvas_modif_row.create_window(5 + self.taille_x_case * element, 5, anchor='nw', window=self.liste_text_row[-1])

    def valid_modify_row(self):
        liste_str=[]
        for element in self.liste_text_row:
            txt=element.get(0.0,'end')
            liste_str.append(txt[:-1])
        self.boss.change_data_row_focus(liste_str)

    def new_row(self):
        liste_text=[]
        for element in self.liste_text_row:
            liste_text.append(element.get(0.0,'end')[0:-1])
        self.boss.add_new_row_to_table(liste_text)

    def delete_row(self):
        self.boss.delete_row_to_table()

