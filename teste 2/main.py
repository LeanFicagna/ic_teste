# ---- Teste 2 Transformação de dados ----- Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo.Tarefas de código:
#
# Extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
# Salvar dados em tabelas estruturadas, em csvs;
# e Zipar todos os csvs num arquivo "Teste_{seu_nome}.zip".

import zipfile
import os
import tabula
import pandas as pd

# Aponta para o arquivo dentro da pasta 'teste 1'
arquivo = '../teste 1/arquivo.pdf'

# Como as tabelas do pdf não estão bem distiguíveis para o extrator de tabelas - tabula -, tentamos deixar a pesquisa o mais precisa possível limitando as páginas que vão ser analisadas
paginas = list(range(114,121))

dfs = tabula.read_pdf(arquivo, pages=paginas, multiple_tables=True)

# Obtem a tabela: Quadro 30

q30 = dfs[0]

q30.columns = q30.iloc[0]
q30 = q30.drop(0)

q30[q30.columns.str.split(' ', 1)[0]] = q30[q30.columns[0]].str.split(' ', 1, expand=True)

q30 = q30.drop(columns=[q30.columns[0]])

q30.to_csv('quadro_30.csv')

# Obtem e formata a tabela: Quadro 32

q32 = dfs[-1]

q32[[q32.iloc[0][0], q32.iloc[1][0]]] = q32[q32.columns[0]][2:].str.split(' ', 1, expand=True)

indexRemove = q32.loc[(q32[q32.columns[0]] != q32[q32.columns[0]]) | (q32[q32.columns[1]] != q32[q32.columns[1]])].index
q32 = q32.drop(indexRemove).drop(columns=q32.columns[0])
q32 = q32.reset_index(drop=True)

q32.to_csv('quadro_32.csv')

# Obtem e formata a tabela: Quadro 31

q31 = dfs[1].rename(columns={dfs[1].columns[0]: dfs[1].loc[0][0], dfs[1].columns[1]:dfs[1].loc[0][1]}).drop(0).reset_index(drop=True)

# Como o extrator de tabelas interpretou que as tabelas do quadro 31 de páginas como se fosse novas tabelas, temos que juntar elas
b = pd.DataFrame()
for a in dfs[2:-1]:
    a.loc[-1] = [a.columns[0], a.columns[1]]
    a.index = a.index + 1
    a = a.sort_index().reset_index(drop=True)
    a = a.rename(columns={a.columns[0]: q31.columns[0], a.columns[1]:q31.columns[1]})
    b = pd.concat([b, a])
q31 = pd.concat([q31, b]).reset_index(drop=True)

q31.to_csv('quadro_31.csv')

# zippar os csv criados
with zipfile.ZipFile('Teste_Leanderson_Ficagna.zip', mode='w') as z:
    z.write('quadro_30.csv')
    z.write('quadro_31.csv')
    z.write('quadro_32.csv')

# delata os csv que não estão dentro do zipp
os.remove('quadro_30.csv')
os.remove('quadro_31.csv')
os.remove('quadro_32.csv')
