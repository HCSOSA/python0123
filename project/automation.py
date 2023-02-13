import pandas as pd
import os
import db
import requests

historicoDolar=[]

message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
print(message)
e=input('ingrese opcion: ')

if(e!='1' or e!='2'):
        if e=='1':
            
            url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
            res=requests.get(url)
            data=res.json()

            dolar_compra=data['compra']
            dolar_venta=data['venta']

            while True:
                V_cambio=float(input('ingrese la cantidad a cambiar'))
                print(dolar_compra*V_cambio)

        elif e=='2':                   
            b=float(input('Ingrese nuevo valor USD: '))
            if b>=5:
                print('fuera de rango')
            else:
                historicoDolar.append(b)
                print(historicoDolar)

else:
    print("Digite caracter correcto")
