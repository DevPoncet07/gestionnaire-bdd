from tkinter import *

class Root(Tk):
	def __init__(self,mode_os):
		self.mode_os=mode_os
		Tk.__init__(self)
		
		
if __name__=="__main__":
	root=Root("tablette")
	root.mainloop()