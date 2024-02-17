from calc_mensualidades_metodos import mensualidades, variables_calculo
from precios import precios
import streamlit as st
import time

st.set_page_config(
        page_title="AM - Mensualidades",
)
def prints(precio, separacion, anticipo, ant, restante, paquete):
    st.write(f'Total a pagar {paquete}: $ {precio:.2f}')
    st.write(f'Separacion: $ {separacion}')
    st.write(f'Anticipo: {anticipo}%')
    st.write(f'Anticipo: $ {ant:.2f}')
    st.write(f'Restante $ {restante}')

#logo de adriana 
st.image('img/LOGO MORADO.png')
#st.title('Adriana Martínez - Wedding Planner')
st.header('Calculadora de mensualidades')

precio = 0.0

anticipo = st.text_input("Porcentaje de anticipo 👇", placeholder='30, 40, 50')
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
    precio = precios('Wedding Experience')
    ant, restante = variables_calculo(precio,separacion,porc_anticipo)

    prints(precio,separacion,anticipo,ant,restante,'Wedding Experience')
    
    df = mensualidades(precio,meses_a_pagar, separacion, ant)
    with st.spinner('Generando...'):
        time.sleep(2)
        st.dataframe(df)


if st.button('AM - Wedding Day', use_container_width=True):
    precio = precios('Wedding Day')
    ant, restante = variables_calculo(precio,separacion,porc_anticipo)

    prints(precio,separacion,anticipo,ant,restante,'Wedding Day')

    df = mensualidades(precio,meses_a_pagar, separacion, ant)
    with st.spinner('Generando...'):
        time.sleep(2)
        st.dataframe(df)

if st.button('AM - Wedding Dream', use_container_width=True):
    precio = precios('Wedding Dream')
    ant, restante = variables_calculo(precio,separacion,porc_anticipo)

    prints(precio,separacion,anticipo,ant,restante,'Wedding Dream')

    df = mensualidades(precio,meses_a_pagar, separacion, ant)
    with st.spinner('Generando...'):
        time.sleep(2)
        st.dataframe(df)