#Este script foi desenvolvido para treinar o uso da biblioteca Tabula(e similares) para extração de dados de tabelas em arquivos .pdf

from tabula.io import read_pdf
from itertools import repeat
import pandas as pd
import tabula
import os
import re


new_list = []
cp = []
contri = []
prop = []
t = 0

#extrai o dado bruto dos arquivos
lista_tabelas = tabula.read_pdf('certidão.pdf', pages="all")

#tratamento para filtrar informações
tab1 = lista_tabelas[0]
tab_com = tab1.head(4)
tab_com.rename(columns={"Unnamed: 0": "adress"}, inplace=True)
tab_com.drop([0, 1], axis=0, inplace=True)
pop = tab_com
pop.drop(['Certidão de Dados Cadastrais do Imóvel - IPTU 2022'], axis=1, inplace=True)
new_list.extend(repeat(pop, 1))
tab2 = tab1.head(20)
cont = tab2['Certidão de Dados Cadastrais do Imóvel - IPTU 2022'][0]
bui = re.findall('[0-9]+', cont)
for trinca in bui:
contribuinte = ''.join(bui)  
d=contribuinte
tab3 = tab2["Unnamed: 0"]
df = pd.DataFrame(tab3)
df.rename(columns={"Unnamed: 0": "adress"}, inplace=True)
df.drop([0, 1, 2, 3, 4, 5, 6, 7], axis=0, inplace=True)
se = df[df.adress.str.contains('CPF ')]
ji = []
ji = str(df[df.adress.str.contains('CPF ')])
nu = ji.replace('CPF ', '')
io = nu.replace('.', '')
ui = io.replace('-', '')
new = str(ui)
fac = re.findall('[0-9-X]+', new)
for fa in fac:
cpf = ''.join(fac)
tab8 = tab2
tab8.drop([0, 1, 2, 3, 4, 5, 6, 7,8], axis=0, inplace=True)
tab8.dropna(inplace=True)
tab8.rename(columns={"Certidão de Dados Cadastrais do Imóvel - IPTU 2022": "propie"}, inplace=True)
df2=pd.DataFrame()

#mergir/fundir os dados filtrados para formar tabelas
df2['comb'] = tab8["Unnamed: 0"] + '&' + tab8["propie"]
ji2 = []
ji2 = str(df2[df2.comb.str.contains('CPF ')])
nu2 = ji2.replace('CPF ', '')
ir = nu2.replace('.', '')
io2 = ir.replace(' ', '¬')

#substituição de caracteres indesejados
new2 = str(io2)
own = re.findall('&[^,;\s]+', new2)
vap = str(own)
te = vap.replace('¬', ' ')
te2 = te.replace('&', '')

#formatação e padronização dos dados/strings para boa visualização
minu = str(te2)
minu = te2.lower()
nome = minu.title()


#Dado a presença de dados sensíveis, optei por não postar o arquivo pdf no repositório público, mesmo que estes sejam de domínio público (dados de imóveis à leilão)
#Dado a complexidade dos binários dos arquivos pdf, nem sempre a ferramenta Tabula será a ideal, sendo necessário fazer tentativas utilizando outras biliotecas e estudos de caso para adequar a melhor forma de extração e requisitos de sistema.



