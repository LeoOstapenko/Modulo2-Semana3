import sqlite3
conexao = sqlite3.connect('ativ_m2s3.sqlite3')
cursor = conexao.cursor()

sql = '''
CREATE TABLE fornecedor (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100) NOT NULL,
    endereco TEXT(100) NOT NULL,
    produto TEXT(100) NOT NULL
);
'''

cursor.execute(sql)

conexao.commit() 
conexao.close()