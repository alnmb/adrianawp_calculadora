from datetime import datetime
from dateutil.relativedelta import relativedelta

def mensualidades(meses, restante, anticipo):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%m-%Y")

    print(f"La fecha actual es {formatted_date}.")
    ciclo = calculo_ciclo(meses)
    mensualidades = restante / 3
    new_date = current_date
    print('Plan de pagos: ')
    for i in range(1, ciclo):
        new_date = new_date + relativedelta(months=1)
        formatted_date = new_date.strftime("%m-%Y")
        if i == 1:
            print(f'Mensualidad {i}: Anticipo')
            print(f'{formatted_date}: $ {anticipo:.2f}')
        else:
            print(f'Mensualidad {i}: ')
            print(f'{formatted_date}: $ {mensualidades:.2f}')

def calculo_ciclo(meses):
    #3 meses hace ciclo range(1,5) veces
    #6 meses hace ciclo range(1,8) veces
    #9 meses hace ciclo range(1,11) veces
    #12 meses hace ciclo range(1,13) veces
    if meses == 3:
        return 5
    elif meses == 6:
        return 8
    elif meses == 9:
        return 11
    elif meses == 12:
        return 13


def main():
    precio_inicial = int(input('Ingrese el precio inicial del paquete\n>> '))
    separacion = int(input('Ingrese la cantidad de separacion\n>> '))
    anticipo_sugerido = (int(precio_inicial) - int(separacion)) * 0.3
    print(f'\nEl anticipo sugerido es de: {anticipo_sugerido}')
    
    cambiar_anticipo = input('\nDesea aumentar su anticipo? Y/N\n>> ')
    if cambiar_anticipo.upper() == 'Y':
        anticipo_sugerido = int(input('Ingrese el porcentaje de anticipo: \n>> '))
        anticipo_sugerido = (int(precio_inicial) - int(separacion)) * anticipo_sugerido/100
        print(f'El anticipo sugerido ahora es de: {anticipo_sugerido}')

    restante = precio_inicial - anticipo_sugerido
    print('Resta de pagar: {}'.format(restante))

    opcion_meses = input('Deseas pagar en 3, 6, 9 o 12 mensualidades?\n>> ')
    mensualidades(int(opcion_meses), restante, anticipo_sugerido)
                





if __name__ == '__main__':
    main()