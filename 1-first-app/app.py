# SETUP

import streamlit as st
import pandas as pd


#-------------------
# CREATE DATA

# Simple dataframe erzeugen
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#2 Spalten A und B
#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title("Meine erste APP")
# Add header
st.header("Mein Header")
# Add a gif from https://giphy.com/
# Bei Giphy auf Share klicken und dann den Link kopieren
# [] Hier kommt Alternativ-Text rein
# () Hier kommt Link rein
st.markdown("![Happy Birthday](https://media.giphy.com/media/m4Z4bII5YUPft1SMDx/giphy.gif)")
st.image('hdm-logo.jpg')

#-------------------
# BODY

#-------------------
# Show static DataFrame

st.dataframe(df)

#-------------------
# Bar chart
st.bar_chart(df)

#SIDEBAR
add_selectbox = st.sidebar.selectbox(
    "Menü",
    ("Aufgabe 1", "Aufgabe 2", "Aufgabe 3")
)

# SLIDER - WIDGET

age = st.slider('FALLSTUDIE 2 (WIE ALT BIST DU?)', 0, 130, 25)
st.write("I'm ", age, 'years old')

# d= st.sidebar.date_input(
# "When's your")
# Weil es im Bootstrap-Format ist, passt sich das Fenster an und wird mitskaliert
# Einfaches Dashboard in Python mit Steamlit
# Für Fallstudie: Mit Streamlit eine Dashboard-App auen, um die Daten zu visualisieren