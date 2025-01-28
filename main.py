from tkinter import Tk
import platform

from src.gestionbdd import GestionBdd

class Root(Tk):
	def __init__(self,mode_os):
		self.mode_os=mode_os
		Tk.__init__(self)
		self['bg']="grey30"
		

		if mode_os=='Windows':
			from interface.interfacedesktop import InterfaceDesktop
			self.interface = InterfaceDesktop(self)
			self.interface.grid()
		else:
			from interface.interfacetablette import InterfaceTablette
			self.interface = InterfaceTablette(self)
			self.interface.grid()
			
		self.gestionbdd=GestionBdd(self)
			
		
		
if __name__=="__main__":
	plat_form=platform.system()
	root=Root(plat_form)
	root.mainloop()
