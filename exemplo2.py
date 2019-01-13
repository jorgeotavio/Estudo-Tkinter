from tkinter import *
'''
	Manipulação de frames, nesse código é feita uma
	manipulação de 6 botões, para organizá-los em forma 
	de pirâmide, utilizando 3 frames, o primeiro com um
	botão, o segundo com dois botões e o terceiro com 3 
	botões. Na função pack() o parâmetro padrão é o side=TOP
	caso não seja definida a side, esse padrão será usado.
'''
class Packing:
	def __init__(self, instancia_tk):

		#criando os containers
		self.container1 = Frame(instancia_tk)
		self.container2 = Frame(instancia_tk)
		self.container3 = Frame(instancia_tk)
		
		#fazendo eles ficarem visiveis um acima do outro
		self.container1.pack()
		self.container2.pack()
		self.container3.pack()

		#criando os botões
		self.b1 = Button(self.container1, text='B1')
		self.b2 = Button(self.container2, text='B2')
		self.b3 = Button(self.container2, text='B3')
		self.b4 = Button(self.container3, text='B4')
		self.b5 = Button(self.container3, text='B5')
		self.b6 = Button(self.container3, text='B6')

		#fazendo os botões ficarem visíveis e definindo as sides dos que precisam
		self.b1.pack()
		self.b2.pack(side=LEFT)
		self.b3.pack(side=LEFT)
		self.b4.pack(side=LEFT)
		self.b5.pack(side=LEFT)
		self.b6.pack(side=LEFT)

raiz = Tk()
Packing(raiz)
raiz.mainloop()