import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQAmthtBSdwG7-ReYch2jjNsgVLqUSDG-BWEnNaS6KiikdNO50cRyP0qcoycjF8sEmciXIjEnMLqrAR/pubhtml#'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    
soup = BeautifulSoup(html_content, 'html.parser')

#Pegar os filtros para cada continente
Tab = soup.find('div', id='top-bar')
dados_tab = [dadosT.text.strip() for dadosT in Tab.find_all('a')]
st.set_page_config(layout="wide")

#Função para obter as informações de cada tabela
def obterInformacoes(cont, lista):
    for dado in cont.find_all('tr')[2:]:
        celulas = dado.find_all('td')
        if celulas:
            name = celulas[1].text.strip()
            skill_rating = celulas[2].text.strip()
            country = celulas[3].text.strip()
            lista.append({'Nome': name, 'Skill Rating': skill_rating, 'País': country})
    return lista

#Pegando os dados de cada continente e armazenando na respectiva váriavel 
Global = soup.find('div', id="0")
dados_Global = []
glob = obterInformacoes(Global, dados_Global)
df_global = pd.DataFrame(glob)

Africa = soup.find('div', id="1110581121")
dados_Africa = []
africa = obterInformacoes(Africa, dados_Africa)
df_africa = pd.DataFrame(africa)

AsiaNorth = soup.find('div', id="504717408")
dados_AsiaNorth = []
asiaN = obterInformacoes(AsiaNorth, dados_AsiaNorth)
df_asiaNorth = pd.DataFrame(asiaN)

AsiaSouth = soup.find('div', id="869681609")
dados_AsiaSouth = []
asiaS = obterInformacoes(AsiaSouth, dados_AsiaSouth)
df_asiaSouth = pd.DataFrame(asiaS)

Europe = soup.find('div', id="1393536766")
dados_Europe = []
eur = obterInformacoes(Europe, dados_Europe)
df_europe = pd.DataFrame(eur)

LatAmNorth = soup.find('div', id="1684642927")
dados_LatAmNorth = []
latNorth = obterInformacoes(LatAmNorth, dados_LatAmNorth)
df_latAmNorth = pd.DataFrame(latNorth)

LatAmSouth = soup.find('div', id="1238511249")
dados_latAmSouth = []
latSouth = obterInformacoes(LatAmSouth, dados_latAmSouth)
df_latAmSouth = pd.DataFrame(latSouth)

MiddleEast = soup.find('div', id="2026239178")
dados_MiddleEast = []
middleE = obterInformacoes(MiddleEast, dados_MiddleEast)
df_middleEast = pd.DataFrame(middleE)

NorthAmerica = soup.find('div', id="1311002172")
dados_NorthAmerica = []
northA = obterInformacoes(NorthAmerica, dados_NorthAmerica)
df_northAmerica = pd.DataFrame(northA)

Oceania = soup.find('div', id="745253575")
dados_Oceania = []
ocen = obterInformacoes(Oceania, dados_Oceania)
df_oceania = pd.DataFrame(ocen)

#Cria caixa de seleção de continente e logo
st.sidebar.image('Assets\EA Sport FIFA 23.png', width=200, use_column_width=True)
continente = st.sidebar.selectbox("Continente",dados_tab)

#Faz a verificação da Select-Box e cria a Barra de pesquisa + Botão de Procura
def apresentarTabela(df):
    barraPesquisa = st.text_input('Pesquisar Nome: ')
    st.button("Search")
    st.write(df)
    if barraPesquisa:
        pesquisa = df[df['Nome'].str.contains(barraPesquisa, case=False)]
        if pesquisa.empty:   
            st.text('Player não Encontrado')  
            st.write(pesquisa)
        else:
            st.text('Player Encontrado')
            st.write(pesquisa)

if continente == "Overview":
    placements = {'Placements': ['Europe - 512', 'LatAm South - 128', 'LatAm North - 128', 'Middle East - 128', 'North America - 128', 
                'Africa - 32', 'North Asia - 64', 'South Asia - 64','Oceania - 32'],
                  'Skill Rating': ['Europe - 1000', 'LatAm South - 820', 'LatAm North - 700', 'Middle East - 860', 'North America - 700', 
                'Africa - 900', 'North Asia - 810', 'South Asia - 810', 'Oceania - 710']
                  }
    st.title("_FGS 23 FUT Division Rivals Leaderboard_ :soccer:" )
    st.dataframe(placements)
    
if continente == "Global":
    apresentarTabela(df_global)

if continente == "Africa":
    apresentarTabela(df_africa)

if continente == "Asia North":
    apresentarTabela(df_asiaNorth)

if continente == "Asia South":
    apresentarTabela(df_asiaSouth)

if continente == "Europe":
    apresentarTabela(df_europe)

if continente == "LatAm North":
    apresentarTabela(df_latAmNorth)

if continente == "LatAm South":  
    apresentarTabela(df_latAmSouth)

if continente == "Middle East":
    apresentarTabela(df_middleEast)
    
if continente == "North America":
    apresentarTabela(df_northAmerica)
    
if continente == "Oceania":
    apresentarTabela(df_oceania)
