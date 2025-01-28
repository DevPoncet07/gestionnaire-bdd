from tkinter import Frame,Canvas


class InterfaceTablette(Frame):
	def __init__(self,boss):
		self.boss=boss
		Frame.__init__(self,master=boss,bg="grey30")
		
		self.can=Canvas(self,width=500,height=500,bg='white')
		self.can.grid(row=0,column=0)