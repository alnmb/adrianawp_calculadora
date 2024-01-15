from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

def variables_calculo(precio, separacion, porc_anticipo):
    anticipo = precio * porc_anticipo
    restante = precio - separacion
    return anticipo, restante

def mensualidades(precio,meses, separacion, anticipo):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m-%Y")

    total = precio - anticipo - separacion
    mensualidades = total / meses  # Calculate monthly installment amount

    data = {'Mensualidad': [], 'Fecha': [], 'Monto': []}

    for i in range(1, meses+2):
        current_date = current_date + relativedelta(months=1)
        formatted_date = current_date.strftime("%m-%Y")
        
        monto = anticipo if i == 1 else mensualidades
        data['Mensualidad'].append(f'Mensualidad {i}: Anticipo' if i == 1 else f'Mensualidad {i}: ')
        data['Fecha'].append(formatted_date)
        data['Monto'].append(f'$ {round(monto, 2)}')

        df = pd.DataFrame(data)
        df = df.set_index('Mensualidad')
    return df