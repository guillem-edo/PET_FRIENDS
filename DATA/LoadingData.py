import pandas as pd
import os
def Loading_data():
    import pandas as pd
    try:
        os.chdir(r"DATA")
        df = pd.read_csv('Amigos_De_Las_Mascotas_2022_Data_Set.csv',sep=';')
        print('[+] Archivo leido')  
        return df
    except Exception as e:
        print('[-] Error al cargar archivo')
        print(e)