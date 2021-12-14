# Tarefas de Preparação:
#
# Baixar os arquivos dos últimos 2 anos no repositório público : http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/ (pode ser feito manualmente)
# Baixar csv do link: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss (pode ser feito manualmente)
# Tarefas de código:
#
# Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação num banco MySQL ou Postgres (Atenção ao encoding dos arquivos!)
# Montar uma query analítica que traga a resposta para as seguintes perguntas:
# Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
# Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
#
#
# Como não há nenhum arquivo csv no link: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss,
# foi considerado apenas os arquivos do: http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
#
# Certifique-se de deixar a pasta 'dados' na raiz do disco C. Caso a idetificação seja por outra label, troque os caminhos no código fonte
# do arquivo load_dados.sql
#
#