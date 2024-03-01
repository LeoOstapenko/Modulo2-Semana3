import sqlite3
conexao = sqlite3.connect('ativ_m2s3.sqlite3')
cursor = conexao.cursor()

sql = '''
UPDATE fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2
'''
cursor.execute(sql)

conexao.commit() 
conexao.close()