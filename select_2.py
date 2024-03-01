import sqlite3
conexao = sqlite3.connect('ativ_m2s3.sqlite3')
cursor = conexao.cursor()

sql = '''
SELECT * FROM fornecedor
WHERE produto = 'Carnes'
'''
resultados = cursor.execute(sql)

for resultado in resultados:
    print(resultado)

print('--------------------------------------------------------------')

conexao.close()