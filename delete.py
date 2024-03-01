import sqlite3
conexao = sqlite3.connect('ativ_m2s3.sqlite3')
cursor = conexao.cursor()

sql = '''
DELETE FROM fornecedor WHERE id = 1;
'''

cursor.execute(sql)

conexao.commit()
conexao.close()