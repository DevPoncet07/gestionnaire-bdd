from tkinter import Frame, Canvas, Text, Entry, Label, StringVar, ALL, Button, Toplevel, Listbox,LabelFrame,Scrollbar
import os


class InterfaceDesktop(Frame):
    def __init__(self, boss,path):
        self.boss = boss

        Frame.__init__(self, master=boss, bg="grey30",width=500,height=500)
        self.path=path
        self.fenetre=None

        self.frame_outils_left=Frame(self,bg='grey30')
        Button(self.frame_outils_left,text="Open bdd",command=self.sortie_button_open_bdd).grid(row=0,column=0)
        self.frame_outils_left.grid(row=0,column=0)

        self.frame_canvas=Frame(self,bg='grey30')
        self.can = Canvas(self.frame_canvas, width=800, height=500, bg='grey20',scrollregion=(0,0,500,600))
        self.can.grid(row=0, column=0)
        self.scroll_x = Scrollbar(self.frame_canvas, orient="horizontal",command=self.can.xview)
        self.scroll_x.grid(row=1, column=0,sticky='ew')
        self.scroll_y = Scrollbar(self.frame_canvas, orient="vertical",command=self.can.yview)
        self.scroll_y.grid(row=0, column=1,sticky='ns')
        self.can.config(xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.frame_canvas.grid(row=0,column=1,padx=10,pady=10)


        self.frame_entry=Frame(self,bg='grey30')
        self.frame_entry.grid(row=0,column=2)
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
        longueur_data=len(data)
        largeur_data=len(names_colonne)
        scrollregion=[0,0,500,500]
        if largeur_data>=6:
            self.can.configure(width=620)
        else:
            self.can.configure(width=20+largeur_data*100)
        scrollregion[2] = 20+largeur_data*100
        scrollregion[3]=50+longueur_data*25
        self.can.config(scrollregion=scrollregion)
        for index in range(largeur_data):
            self.can.create_rectangle(5+index*100,5,100+index*100,30,outline="white")
            self.can.create_text(30+index*100,10,anchor="nw",text=names_colonne[index],fill='white')
            for element in range(longueur_data):
                self.can.create_window(10+index*100,50+element*25,anchor="nw",window=EntryCell(self.can,data[element][index]))

    def sortie_button_open_bdd(self):
        self.fenetre=FenetreOpenBdd(self,self.path)

    def sortie_fenetre_openbdd(self,name):
        self.fenetre.destroy()
        self.boss.charger_base_de_donnee(name)

class FenetreOpenBdd(Toplevel):
    def __init__(self,boss,path):
        self.boss=boss
        Toplevel.__init__(self)
        self.geometry("500x500+100+100")
        self.title("Open database")
        self['bg']='grey30'
        names=os.listdir(path+"/base_de_donnee")
        self.names_bdd=[]
        for name in names:
            self.names_bdd.append(name[:-3])

        self.frame_dossier=LabelFrame(self,text="Bdd Dossier")
        self.listbox_dossier_bdd=Listbox(self.frame_dossier,height=7,width=15)
        self.listbox_dossier_bdd.grid(padx=10,pady=10)
        for name in self.names_bdd:
            self.listbox_dossier_bdd.insert('end',name)
        self.listbox_dossier_bdd.bind("<ButtonRelease-1>",self.sortie_listbox_dossier_bdd)
        self.frame_dossier.grid(row=0,column=0,padx=10,pady=10)


        self.frame_infos=LabelFrame(self,text='Information Bdd')
        self.str_name_bdd=StringVar()
        self.str_name_bdd.set("")
        self.label_str_name_bdd=Label(self.frame_infos,textvariable=self.str_name_bdd)
        self.label_str_name_bdd.grid(row=0,column=0)
        Button(self.frame_infos,text='Charger Bdd',command=self.sortie_self).grid(row=1,column=0)
        self.frame_infos.grid(row=1,column=0)

    def sortie_listbox_dossier_bdd(self,event):
        index=self.listbox_dossier_bdd.curselection()
        name=self.names_bdd[index[0]]
        self.mise_a_jour_frame_infos([name])

    def mise_a_jour_frame_infos(self,infos):
        self.str_name_bdd.set('Bdd names : '+str(infos[0]))

    def sortie_self(self):
        name=self.str_name_bdd.get()[12:]
        if name!="":
            self.boss.sortie_fenetre_openbdd([name])




class EntryCell(Text):
    def __init__(self,boss,text):
        Text.__init__(self,master=boss,width=10,height=1)
        text=str(text)
        self.insert('end',text)

