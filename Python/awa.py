from tkinter import *
import sqlite3

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Python + TKInter + BD (Sqlite)')
        self.janela.geometry('610x180')
        self.janela.eval('tk::PlaceWindow . center')
        self.janela.resizable(width = False, height = False)
        self.operacao = ''

        self.Button1 = Button(background = 'green',
                              font = 'Arial 12 bold',
                              foreground = 'white',
                              text = 'Inserir',
                              command = self.inserir
                              )
        self.Button1.place(x = 510, y = 9,
                           height = 35,
                           width = 96)
        self.Button2 = Button(background = 'yellow',
                              font = 'Arial 12 bold',
                              text = 'Consultar', )
        self.Button2.place(x = 508, y = 57,
                           height = 36,
                           width = 98)
        self.Button3 = Button(background = 'red',
                              font = 'Arial 12 bold',
                              foreground = 'white',
                              text = 'Apagar')
        self.Button3.place(x = 505,
                           y = 142,
                           height = 31,
                           width = 100)
        self.Button4 = Button(background = 'orange',
                              font = 'Arial 12 bold',
                              text = 'Alterar')
        self.Button4.place(x = 507,
                           y = 102,
                           height = 31,
                           width = 99)
        self.Button5 = Button(font = 'Arial 12 bold',
                              text = 'OK',
                              command=self.ok )
        self.Button5.place(x = 297,
                           y = 124,
                           height = 47,
                           width = 195)
        self.Entry1 = Entry(borderwidth = 3,
                            font = 'Arial 16 bold',
                            foreground = 'blue',
                            justify = 'left')
        self.Entry1.place(x = 119,
                          y = 64,
                          height = 47,
                          width = 380)
        self.Entry2 = Entry(borderwidth = 3,
                            font = 'Arial 16 bold',
                            foreground = 'blue',
                            justify = 'left')
        self.Entry2.place(x = 117,
                          y = 122,
                          height = 48,
                          width = 161)
        self.Label1 = Label(background = 'Black',
                            borderwidth = 2,
                            font = 'Arial 25 bold',
                            foreground = 'White',
                            text = 'Agenda Internacional')
        self.Label1.place(x = 5,
                          y = 4,
                          height = 50,
                          width = 497)
        self.Label2 = Label(font = 'Arial 16 bold',
                            text = 'Nome:')
        self.Label2.place(x = 12,
                          y = 72,
                          height = 30,
                          width = 70)
        self.Label3 = Label(font = 'Arial 16 bold',
                            text = 'Telefone:')
        self.Label3.place(x = 6,
                          y = 133,
                          height = 30,
                          width = 111)

        self.janela.mainloop()
    def inserir(self):
            self.Entry1.delete(0,END)
            self.Entry2.delete(0,END)
            self.operacao = 'inserir'
    def ok(self):
        con = sqlite3.connect('agenda.db')
        sql = con.cursor()
        if self.operacao == 'inserir':
            try:
                 sql.execute('CREATE TABLE registro (nome,telefone)')
            except:
                sql.execute('INSERT INTO registro(nome,telefone) VALUES(?,?)',(self.Entry1.get(),self.Entry2.get()))
                con.commit()
                con.close()

aplicacao=App()