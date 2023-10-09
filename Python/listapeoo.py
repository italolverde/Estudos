from tkinter import *
persistencia = False
agendadic = {}
class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('790x400')
        self.janela.title('030 - Serialização e Persistência')

        self.canvas1 = Canvas(self.janela, width=790, height=400)
        self.canvas1.pack()

        self.titulo1 = Label(
            self.canvas1,
            text='Agenda Internacional',
            width=52,
            height=2,
            bg='black',
            font='Arial 20 bold',
            fg='white',
            borderwidth=5,
            relief='raised',
        )
        self.titulo1.place(x=0,y=0)

        self.canvas1.create_line(
            550,1,
            550,400,
            dash = (5,2)
        )

        self.canvas1.create_rectangle(
            10,337,
            540,390
        )

        self.tituloLeitura = Label(
            self.canvas1,
            width=24,
            fg='blue',
            text='Leitura/Desserialização',
            bg='white',
            font='Helvetica 12'
        )
        self.tituloLeitura.place(x=560,y=80)

        self.textoNome1 = Label(
            self.canvas1,
            text='Nome do Arquivo: ',
            font='Helvetica 15'
        )
        self.textoNome1.place(x=560,y=110)

        self.nomeArq1 = Entry(
            self.canvas1,
            width=21,
            font='Helvetica 14'
        )
        self.nomeArq1.place(x=560,y=140)

        self.BotaoLer = Button(
            self.canvas1,
            width=20,
            text='Ler/Desserializar',
            bg='blue',
            fg='white',
            font='Helvetica 14'
        )
        self.BotaoLer.place(x=560,y=180)

        self.canvas1.create_line(
            550,233,
            785,233,
            dash = (5,2)
        )

        self.tituloGravacao = Label(
            self.canvas1,
            width=24,
            fg='red',
            text='Serialização/Persistência',
            bg='white',
            font='Helvetica 12'
        )
        self.tituloGravacao.place(x=560,y=250)

        self.textoNome2 = Label(
            self.canvas1,
            text='Nome do Arquivo: ',
            font='Helvetica 15'
        )
        self.textoNome2.place(x=560,y=280)

        self.nomeArq2 = Entry( #
            self.canvas1,
            width=21,
            font='Helvetica 14'
        )
        self.nomeArq2.place(x=560,y=310)

        self.botaoGravar = Button(
            self.canvas1,
            width=20,
            text='Serializar/Gravar',
            bg='red',
            fg='white',
            font='Helvetica 14'
        )
        self.botaoGravar.place(x=560,y=350)

        self.botaoModoInclusao = Button(
            self.canvas1,
            text='Modo Inclusão',
            width=26,
            height=2,
            command = self.habilitaInclusao
        )
        self.botaoModoInclusao.place(x=16,y=340)

        self.botaoModoConsulta = Button(
            self.canvas1,
            text='Modo Consulta',
            width=25,
            height=2,
            command = self.habilitaConsulta
        )
        self.botaoModoConsulta.place(x=283,y=340)

        self.textoNomeAgenda = Label(
            self.canvas1,
            text='Nome:',
            font='Helvetica 14 bold'
        )
        self.textoNomeAgenda.place(x=20,y=100)

        self.caixaNomeAgenda = Entry( #Entry Nome
            self.canvas1,
            font='Helvetica 14 bold'
        )
        self.caixaNomeAgenda.place(x=20,y=135,height=40,width=510)

        self.textoTelefoneAgenda = Label(
            self.canvas1,
            text='Telefone:',
            font='Helvetica 14 bold'
        )
        self.textoTelefoneAgenda.place(x=20,y=190)
 
        self.caixaTelefoneAgenda = Entry( #Entry Telefone
            self.canvas1,
            font='Helvetica 14 bold'
            
        )
        self.caixaTelefoneAgenda.place(x=20,y=225,height=40,width=510)

        self.botaoInserir = Button( #BOTAO INSERIR
            self.canvas1,
            text='Inserir',
            font='Helvetica 12 bold',
            width=17,
            height=2,
            bg='green',
            bd=3,
            fg='white',
            command = self.inserir
        )
        self.botaoInserir.place(x=327,y=273)

        self.janela.mainloop()
          
    def habilitaConsulta(self):
        self.caixaNomeAgenda.delete(0,END)

        self.labelTelefoneAgenda = Label(
            self.canvas1,
            font='Helvetica 14 bold',
            fg='blue',
#            text='Telefone Cadastrado',
            anchor='w'
        )
        self.labelTelefoneAgenda.place(x=20,y=225,height=40,width=510)

        self.botaoConsultar = Button(
            self.canvas1,
            text='Consultar',
            font='Helvetica 12 bold',
            width=17,
            height=2,
            bg='blue',
            bd=3,
            fg='white',
        )
        self.botaoConsultar.place(x=327,y=273)

    def habilitaInclusao(self):
        self.caixaNomeAgenda = Entry(
            self.canvas1,
            font='Helvetica 14 bold'
        )
        self.caixaNomeAgenda.place(x=20,y=135,height=40,width=510)

        self.caixaTelefoneAgenda = Entry(
            self.canvas1,
            font='Helvetica 14 bold'
        )
        self.caixaTelefoneAgenda.place(x=20,y=225,height=40,width=510)

        self.botaoInserir = Button(
            self.canvas1,
            text='Inserir',
            font='Helvetica 12 bold',
            width=17,
            height=2,
            bg='green',
            bd=3,
            fg='white',
        )
        self.botaoInserir.place(x=327,y=273)
    def inserir(self):
        if persistencia:
            with open('agenda.txt', 'a') as agenda:
                agenda.write(self.caixaNomeAgenda.get())
                agenda.write(self.caixaTelefoneAgenda.get())
        else:
            nome = self.caixaNomeAgenda.get()
            telefone = self.caixaTelefoneAgenda.get()
            agendadic[nome] = telefone
            print(agendadic)
    def consultar(self):
        nome = self.caixaNomeAgenda.get()
        if nome in agendadic:
            pass
aplicacao=App()