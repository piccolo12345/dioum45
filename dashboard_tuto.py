import streamlit as st
import pandas as pd
def load_data ()  :
    ## Chargement de la base de donné###
    base1 = pd.read_csv("achats.csv", parse_dates=['timestamp'])
    base2 = pd.read_csv("clics.csv", parse_dates=['timestamp'])
    base3 = pd.read_csv("impressions.csv", parse_dates=['timestamp'])
    base_n = pd.merge(base3, base2, on='cookie_id', how='left')
    base = pd.merge(base_n, base1, on='cookie_id', how='left')
    return base

#Titre du dashboard
st.title("Mon application Streamlit")
st.write("Bienvenue sur mon application !")

#Ajout d'un side bar
check_box = st.sidebar.checkbox(label = 'display dataset')
st.sidebar.subheader("Paramètres de visualisation")

st.sidebar.file_uploader(label = "Chargez vos fichiers csc")

df = load_data()
st.write(df)

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Add traces to each subplot
#fig.add_trace(go.Scatter(x=x, y=y1, name='Plot 1'), row=1, col=1)

# Un premier exemple
exemple = go.Figure(
    data=[go.Bar(y=df['age'])],
    layout_title_text="A Figure Displayed with fig.show()"
)
st.write(exemple)

# Chiffre d'affaire

chif_affaire = df['price'].sum()

st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chif_affaire} € </span>", unsafe_allow_html=True)

#Nombre de clics par heure
import plotly.express as px
clic_heure = px.bar(df, x = "timestamp", y = "timestamp_x")
st.write(clic_heure)

#Boxplot des ages en fonction de ID_produit
fig_produit_age = px.box(df, x='product_id', y="age", points="outliers")
st.write(fig_produit_age)

# Evolution du prix
prix_evolution = px.line(df, x = "timestamp_x" , y = 'price',title = "évolution du prix à chaque achat")
st.write(prix_evolution)

