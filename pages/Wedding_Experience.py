import streamlit as st
from metodos_calculos.metodos import mensualidades, variables_calculo, format_precios
from metodos_calculos.precios import precios_totales, precios_expo
from metodos_gui.metodos_gui import print_results, prints


st.set_page_config(
        page_title="Wedding Experience",
)

#logo de adriana 
st.image('img/LOGO AMEP MORADO.png')
st.header('Calculadora de mensualidades')

paquete = 'Wedding Experience'

anticipo = st.text_input("Porcentaje de anticipo 👇", placeholder='30, 50')
if anticipo:
    if anticipo.isdigit():
        porc_anticipo = int(anticipo)/100
    else:
        st.error('Por favor, ingresa un numero')

separacion = st.text_input("Separacion 👇", placeholder='500')
if separacion:
    if separacion.isdigit():
        separacion = float(separacion)
    else:
        st.error('Por favor, ingresa un numero')   

meses_a_pagar = st.selectbox('Meses a financiar 👇',
                             ('3','6','9','12','14','18'), 
                             index=None)

precio_totales = precios_totales(paquete)
precio_expo = precios_expo(paquete)
cotizar = st.button('Cotizar...')
if cotizar:
    try:
        meses_a_pagar = int(meses_a_pagar)
        ant, restante = variables_calculo(separacion,porc_anticipo, precio_expo)
        prints(precio_expo,separacion,anticipo,ant,restante,paquete)
        print_results(precio_expo,meses_a_pagar,separacion,ant)
    except Exception as e:
        st.error(f'Ingrese los datos requeridos en los campos de arriba {e}')