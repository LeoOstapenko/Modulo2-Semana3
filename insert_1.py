nome = input('Digite o Nome do fornecedor: ')
endereco = input('Digite o Endereço do fornecedor: ')
produto = input('Digite o Produto do fornecedor: ')

import sqlite3
conexao = sqlite3.connect('ativ_m2s3.sqlite3')
cursor = conexao.cursor()

sql = 'INSERT INTO fornecedor (nome, endereco, produto) VALUES (?, ?, ?)'
valores = [nome, endereco, produto]

cursor.execute(sql, valores)
conexao.commit()

print('DADO INSERIDO COM SUCESSO!')

conexao.close()