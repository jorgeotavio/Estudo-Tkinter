from tkinter import *
'''
	Foi implementado o label e a função bind que faz com que
	o evento do clique do botao esquerdo do mouse no botão
	mude a cor do widget.
'''
class Janela:
	def __init__(self, toplevel):
		
		self.frame = Frame(toplevel)
		self.frame.pack()

		self.texto = Label(self.frame, text='Clique para ficar amarelo')
		self.texto['width'] = 26
		self.texto['height'] = 3
		self.texto.pack()

		self.botaoverde = Button(self.frame, text='Clique aqui')
		self.botaoverde['bg'] = 'green'
		
		# aqui é onde acontece a mágica
		self.botaoverde.bind("<Button-1>", self.muda_cor)
		self.botaoverde.pack()

	def muda_cor(self, event):

		if self.botaoverde['bg'] == 'green':
			self.botaoverde['bg'] = 'yellow'
			self.texto['text'] = 'Clique para ficar verde'
		else:
			self.botaoverde['bg'] = 'green'
			self.texto['text'] = 'Clique para ficar amarelo'

raiz = Tk()
Janela(raiz)
raiz.mainloop()