import pandas as pd
import streamlit as st
import plotly.express as px
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

#Pegando os dados de cada continente e armazenando na respectiva váriavel 
Global = soup.find('div', id="0")
Africa = soup.find('div', id="1110581121")
AsiaNorth = soup.find('div', id="504717408")
AsiaSouth = soup.find('div', id="869681609")
Europe = soup.find('div', id="1393536766")
LatAmNorth = soup.find('div', id="1684642927")
LatAmSouth = soup.find('div', id="1238511249")
dados_latAm = []
for dado in LatAmSouth.find_all('tr'):
    celulas = dado.find_all('td')
    if celulas:
        name = celulas[1].text.strip()
        skill_rating = celulas[2].text.strip()
        country = celulas[3].text.strip()
        dados_latAm.append({'Nome': name, 'Skill Rating': skill_rating, 'País': country})

MiddleEast = soup.find('div', id="2026239178")
NorthAmerica = soup.find('div', id="1311002172")
Oceania = soup.find('div', id="745253575")

st.set_page_config(layout="wide")

#Criar caixa de seleção de continente
continente = st.sidebar.selectbox("Continente",dados_tab) 

df = pd.DataFrame(dados_latAm)

#Criar Barra de pesquisa e Botão de Procura
pesquisa_nome = st.text_input('Pesquisar Nome: ')
button = st.button("Search")

#Faz a verificação da Select-Box
if continente == "LatAm South":  
    st.write(df)
    if pesquisa_nome:
        pesquisa = df[df['Nome'].str.contains(pesquisa_nome, case=False)]
        st.text('Player Encontrado')  
        st.write(pesquisa)