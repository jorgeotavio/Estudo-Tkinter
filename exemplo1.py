from tkinter import *
'''
	Para gerenciar a janela em com classe
	foi usada a hierarquia, nesse caso o método
	construtor recebe como parâmetro a janela principal
	chamada de toplevel, e a partir dela são criados outros
	frames como o exemplo do botão, seus parâmetros são:
	Button("janela a qual o botão vai pertencer", 
			"texto que será apresentedo no botao", "cor de fundo")
	Mas os widgets em geral podem ser manipulados como
	dicionário, exemplo: self.botao['bg'] = "green"
'''
class Janela:
	def __init__(self, toplevel):
		
		#criando o frame para acoplar os dois botões
		self.fr1 = Frame(toplevel)

		#criando o botão 1 e configurando ele
		self.botao = Button(self.fr1, text='botao1')
		self.botao['bg'] = '#BA55D3' 
		self.botao['font'] = ('impact', '12', 'bold', 'italic')

		#criando o botão 2 e configurando ele
		self.botao2 = Button(self.fr1, text='botao2')
		self.botao2["bg"] = 'red'
		self.botao2['font'] = ('impact', '12', 'bold', 'italic')
		
		#deixando o frame e os botões visivels		
		self.fr1.pack()
		self.botao.pack()
		self.botao2.pack()


raiz = Tk() 	#gerando a janela mãe
Janela(raiz)	#passando ela como parametro para a classe Janela()
raiz.mainloop()	#mantendo o loop de leitura do código