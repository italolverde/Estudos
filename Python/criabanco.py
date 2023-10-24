import sqlite3
try:
    con = sqlite3.connect('agenda.db')
    sql = con.cursor()
    sql.execute('CREATE TABLE registro (nome,telefone')
    print('banco criado com sucesso!')
except:
    pass
