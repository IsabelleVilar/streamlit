import streamlit as st
import pandas as pd

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script

# st.set_page_config(page_title='Streamlit') define o título da página que será exibido na barra de título do navegador

# st.set_page_config(page_icon=':chart_with_upwards_trend:') define o ícone da página que será exibido na barra de título do navegador. Isso normalmente é um arquivo .ico, .png ou .svg

# st.set_page_config(layout='wide') define o layout padrão do aplicativo. Pode ser 'wide', 'centered', ou 'fullscreen'

# st.set_page_config(initial_sidebar_state='auto') define o estado inicial da barra lateral. Pode ser 'auto', 'expanded' ou 'collapsed'

# st.set_page_config(menu_items={'Get Help': 'https://www.extremelycoolapp.com/help', 'Report a bug': "https://www.extremelycoolapp.com/bug",'About': "# This is a header. This is an *extremely* cool app!"}) uma lista de itens de menu personalizados que serão exibidos no canto superior direito do aplicativo

# exemplo usando vários métodos: st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

st.set_page_config(page_title='Meu Site Streamlit')

with st.container(): # st.container agrupa elementos em um contêiner, ajudando na organização do layout do aplicativo
    st.subheader('Meu primeiro site com o Streamlit') # cria um subcabeçalho menor abaixo do cabeçalho principal
    st.title('Dashboard de Contratos') # define o título do aplicativo
    st.write('Informações sobre os contratos fechados no mês de maio') # escrever texto
    st.markdown("Link para entrar na página do Google [Clique aqui](https://www.google.com)") # permite formatar texto usando Markdown para adicionar ênfase, listas, links, etc. Também pode ser usado st.write("[Google](https://www.google.com)")

@st.cache_data # decorator para armazenar funções em cache que retornam dados
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela

with st.container():
    st.write('---')
    qtde_dias = st.selectbox('Selecione o período', ['7 dias', '15 dias', '21 dias', '30 dias'])
    num_dias = int(qtde_dias.replace(' dias', ''))
    dados = carregar_dados()    
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')
