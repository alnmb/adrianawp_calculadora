
import streamlit as st
import pandas as pd


st.set_page_config(
        page_title="Calculadora de Mensualidades",
)

#logo de adriana 
st.image('img/LOGO AMEP MORADO.png')
st.header('Calculadora de mensualidades')

#Tabla de precios
data = {
    "Servicio":              ["Wedding Day","Wedding Dream", "Wedding Experience"],
    "Precio Normal":         ['$ 8,800.00','$ 15,900.00', '$ 29,900.00'],
    "Precio Expo Tu Boda":   ['$ 7,920.00','$ 14,310.00', '$ 26,910.00']
}

df = pd.DataFrame(data)
df.set_index("Servicio", inplace=True)
st.table(df)

st.write('Seleccione el paquete a cotizar...')

#mostrar 3 botones, uno para cada opcion respectivamente
wed_exp = st.button('Wedding Experience')
wed_dream = st.button('Wedding Dream')
wed_day = st.button('Wedding Day')

if wed_exp == True:
    st.switch_page("pages/Wedding_Experience.py")
if wed_dream == True:
    st.switch_page("pages/Wedding Dream.py")
if wed_day == True:
    st.switch_page("pages/Wedding Day.py")
