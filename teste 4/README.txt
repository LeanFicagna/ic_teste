# Baixar csv do link: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss
# Tarefas de código:
#
# Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de preparação) e retorne as linhas que mais se assemelham
# Criar uma interface usando o framework Vue.js que permita a um usuário fazer essa pesquisa pelo browser
#
#
# ################################## Observações ###############################################
#
# Como não há nenhum csv no link https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss,
# foi considerado os dados dos últimos 2 anos do link http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/,
#
#
#
# Para executar o serve primeiro abra um terminal dentro da pasta backend e execute o comando: python app.py
# 
#
# Para rodar o vue.js, entre na pasta frontend, e com o npm e nodejs instalado execute no terminal: npm run serve