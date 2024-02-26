import streamlit as st
import time
from metodos_calculos.metodos import format_precios, mensualidades


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