from tkinter import Tk

from src.gestionbdd import GestionBdd

class Root(Tk):
	def __init__(self,mode_os):
		self.mode_os=mode_os
		Tk.__init__(self)
		
		if mode_os=="tablette":
			from interface.interfacetablette import InterfaceTablette
			self.interface=InterfaceTablette(self)
			self.interface.grid()
			
		self.gestionbdd=GestionBdd(self)
			
		
		
if __name__=="__main__":
	root=Root("tablette")
	root.mainloop()