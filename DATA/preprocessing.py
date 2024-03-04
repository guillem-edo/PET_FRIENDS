import pandas as pd
import matplotlib.pyplot as plt

class preprocessing:
    @staticmethod
    def limpiar_numeros(df, columnas_numericas):
        for columna in columnas_numericas:
            if df[columna].dtype == 'object':
                df[columna] = df[columna].str.replace(',', '.').astype(float)
        
        # Redondear los números con más de dos decimales a dos decimales
                df[columna] = df[columna].apply(lambda x: round(x, 2) if isinstance(x, float) else x)
        return df
    def reemplazar_nulos_con_guion(df):
        # Reemplazar valores nulos por '-'
        df_sin_nulos = df.fillna('-', inplace=True)
    
        # Mostrar mensaje en pantalla
        print(f"[+] Se han reemplazado los valores nulos por ['-'] en el df.")
    
        return df_sin_nulos


def outliers(var):
    #ESTA FUNCION MUESTRA LOS OUTLIERS DE LA BASE DE DATOS
    q1=var.quantile(0.25)
    q3=var.quantile(0.75)
    riq=q3-q1
    sup=q3+1.5*(riq)
    inf=q1-1.5*(riq)
    outl=(var>sup) | (var<inf)
    return outl

def drop_outliers(df,columnas_numericas):
    #ESTA FUNCION ELIMINA LOS OUTLIERS DE LA BASE DE DATOS.
    for i in df.loc[:,columnas_numericas]:
        df=df[~outliers(df[i])]
        return df
