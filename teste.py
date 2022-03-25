import pandas as pd
import sqlite3 as sq

banco = sq.connect('loja.db')
cursor = banco.cursor()
clientes = pd.read_sql('SELECT * FROM cliente', con=banco)
clientes

tabela = pd.read_csv('tabela_condicao.csv')
print(tabela)

pd.concat([clientes, tabela])
left = clientes.set_index(['condicao'])
right = tabela.set_index(['condicao'])
left.join(right, lsuffix='_con')

