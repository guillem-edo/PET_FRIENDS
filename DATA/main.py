from LoadingData import Loading_data
from preprocessing import preprocessing
from preprocessing import outliers
from preprocessing import drop_outliers
from eda import eda

numericas = ['Orden', 'Estado', '%Iva', 'Precio', 'PrecioCoste', '%Descuento', 'ImporteCoste', 'ImporteBruto', 'ImporteNeto', 'BaseImponible', 'TotalIva', 'ImporteLiquido']

if __name__ == '__main__':
    # Cargar datos
    df = Loading_data()

    if df is not None:
        print("[+] Archivo CSV cargado correctamente.")
    else:
        print("[-] No se pudo cargar el archivo CSV.")
        exit(-1)

    # Limpiar números
    df_limpiado = preprocessing.limpiar_numeros(df, numericas)
    print(df_limpiado.sample(10))
    print(df.info())
    # Mostrar outliers y eliminarlos
    outliers(df[numericas])
    df = drop_outliers(df,numericas)
    print("[+] OUTLIERS eliminados CORRECTAMENTE")

    # Reemplazar valores nulos por '-'
    df_sin_nulos = preprocessing.reemplazar_nulos_con_guion(df)

    # Encontrar los productos más vendidos por fecha de registro
    info_productos = eda.productos_mas_vendidos_por_fecha(df_limpiado, '2022-01-01', '2022-12-31')

    # Mostrar los top clientes
    eda.top_clientes(df)

    # Graficar top clientes
    eda.graficar_top_clientes(df, 'NombreColumnaPedidos')

    # Graficar y mostrar top 10 articulos
    eda.graficar_artic_top_10(df)

    # Graficar top meses y año
    eda.top_articulos_y_grafico(df)

    # Top 20 articulos por cada mes del año
    eda.top_20_articulos_por_mes(df)

    eda.graficar_top_articulos_por_familia(df)

    eda.grafico_subfamilias_mas_comunes_por_familia(df)   
    
    #GRAFICO DESCUENTOS
    eda.grafico_descuentos_y_articulos(df)
# Hacer un menú posteriormente con diferentes cosas para hacer de cara al usuario y cerrarlo luego con la 'q'

    eda.grafico_comparativa_precio_coste(df)
    
