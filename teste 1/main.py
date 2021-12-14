#    ---- Teste 1 - WebScraping -----   Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo.Tarefas de código:
#
#    1.1 - Acessar o site: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss;
#    1.2 - Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_201902.pdf);
#    1.3 - Baixar o componente organizacional;

import requests
from bs4 import BeautifulSoup
import wget

url = 'https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss'

try:
    pagina = BeautifulSoup(requests.get(url).content, 'html.parser').find('a', attrs={'class': 'alert-link'})['href']
    link = BeautifulSoup(requests.get(pagina).content, 'html.parser').find('a', attrs={'class': 'internal-link'})['href']

    name = wget.download(link, 'arquivo.pdf')
except:
    print(requests.get(url).status_code)

print(name)
