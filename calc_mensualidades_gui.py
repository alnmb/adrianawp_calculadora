from calc_mensualidades_metodos import mensualidades, variables_calculo, format_precios
from precios import precios_totales, precios_expo
import streamlit as st
import pandas as pd
import time

st.set_page_config(
        page_title="AM - Mensualidades",
)

def prints(precio, separacion, anticipo, ant, restante, paquete):
    st.write(f'Total a pagar {paquete}: {format_precios(precio)}')
    st.write(f'Separacion: {format_precios(separacion)}')
    st.write(f'Adelanto Primera Cita: {anticipo}%')
    st.write(f'Adelanto Primera Cita: {format_precios(ant)}')
    st.write(f'Restante {format_precios(restante)}')

def print_results(precio_expo,meses_a_pagar,separacion,ant):
    df = mensualidades(precio_expo,meses_a_pagar, separacion, ant)
    with st.spinner('Generando...'):
        time.sleep(1)
        st.table(df)

#logo de adriana 
st.image('img/LOGO AMEP MORADO.png')
#st.title('Adriana Martínez - Wedding Planner')
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

precio = 0.0

anticipo = st.text_input("Porcentaje de anticipo 👇", placeholder='30, 50')
if anticipo:
    porc_anticipo = int(anticipo)/100

separacion = st.text_input("Separacion 👇", placeholder='500')
if separacion:
    separacion = float(separacion)

meses_a_pagar = st.text_input('Meses a financiar 👇', placeholder='3,6,9,12')
if meses_a_pagar:
    meses_a_pagar = int(meses_a_pagar)

st.text('Seleccione el paquete a cotizar: ')
if st.button('AM - Wedding Experience', use_container_width=True):
    precio_totales = precios_totales('Wedding Experience')
    precio_expo = precios_expo('Wedding Experience')

    ant, restante = variables_calculo(separacion,porc_anticipo, precio_expo)

    prints(precio_expo,separacion,anticipo,ant,restante,'Wedding Experience')
    print_results(precio_expo,meses_a_pagar,separacion,ant)
    # df = mensualidades(precio_expo,meses_a_pagar, separacion, ant)
    # with st.spinner('Generando...'):
    #     time.sleep(1)
    #     st.table(df)

if st.button('AM - Wedding Day', use_container_width=True):
    precio_totales = precios_totales('Wedding Day')
    precio_expo = precios_expo('Wedding Day')

    ant, restante = variables_calculo(separacion,porc_anticipo, precio_expo)

    prints(precio_expo,separacion,anticipo,ant,restante,'Wedding Day')

    print_results(precio_expo,meses_a_pagar,separacion,ant)

if st.button('AM - Wedding Dream', use_container_width=True):
    precio_totales = precios_totales('Wedding Dream')
    precio_expo = precios_expo('Wedding Dream')

    ant, restante = variables_calculo(separacion,porc_anticipo, precio_expo)

    prints(precio_expo,separacion,anticipo,ant,restante,'Wedding Dream')

    print_results(precio_expo,meses_a_pagar,separacion,ant)