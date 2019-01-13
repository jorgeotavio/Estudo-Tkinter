from tkinter import *

class Passwords:
	def __init__(self, toplevel):

		self.frame1 = Frame(toplevel)
		self.frame2 = Frame(toplevel)
		self.frame3 = Frame(toplevel)
		self.frame4 = Frame(toplevel, pady=10)

		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
		self.frame4.pack()

		font1 = ('Verdana', '14', 'bold')
		font2 = ('Verdana', '10', 'bold')

		Label(self.frame1, text='PASSWORDS', fg='darkblue', font=font1, height=3).pack()
		Label(self.frame2, text='Nome: ', font=font2, width=8).pack(side=LEFT)
		Label(self.frame3, text='Senha: ', font=font2, width=8).pack(side=LEFT)

		self.nome = Entry(self.frame2, width=10, font=font2)
		self.nome.focus_force()
		self.nome.pack(side=LEFT)

		self.senha = Entry(self.frame3, width=10, show='*', font=font2)
		self.senha.pack(side=LEFT)

		self.confere = Button(self.frame4, font=font2, text='Conferir', bg='blue', command=self.conferir)
		self.confere.pack()

		self.msg = Label(self.frame4, font=font2, height=3, text='Aguardando...')
		self.msg.pack()

	def conferir(self):
		NOME = self.nome.get()
		SENHA = self.senha.get()

		if NOME == SENHA:
			self.msg['text'] = 'ACESSO PERMITIDO'
			self.msg['fg'] = 'darkgreen'
		else:
			self.msg['text'] = 'ACESSO NEGADO'
			self.msg['fg'] = 'red'
			self.nome.focus_force()

instancia = Tk()
Passwords(instancia)
instancia.mainloop()