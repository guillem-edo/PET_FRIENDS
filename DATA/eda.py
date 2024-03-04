import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class eda:
    @staticmethod
    def top_clientes(df):
        pedidos_por_cliente = df.groupby('CodigodelCliente').size()
        top_5_clientes = pedidos_por_cliente.sort_values(ascending=False).head(5)

        # Obtener el cliente que realiza más compras
        cliente_mas_compras = pedidos_por_cliente.idxmax()
        
        # Filtrar el DataFrame para obtener solo los pedidos del cliente más activo
        pedidos_cliente_mas_compras = df[df['CodigodelCliente'] == cliente_mas_compras]
        
        # Calcular la frecuencia de compras del cliente más activo
        frecuencia_compras = pedidos_por_cliente.max()
        
        # Calcular el volumen total de compras del cliente más activo
        volumen_compras = pedidos_por_cliente.max()
        
        # Calcular los productos más comprados por el cliente más activo
        productos_mas_comprados = pedidos_cliente_mas_compras['CodigoArticulo'].value_counts().head(5)
        
        # Calcular el valor medio de las compras del cliente más activo
        valor_medio_compras = pedidos_cliente_mas_compras['ImporteLiquido'].mean()
        
        # Imprimir la información relevante
        print("Top 5 de clientes que realizan más compras:")
        print(top_5_clientes)
        print(f"Información sobre el cliente que realiza más compras (Código del cliente: {cliente_mas_compras}):")
        print(f"- Frecuencia de compras: {frecuencia_compras}")
        print(f"- Volumen total de compras: {volumen_compras}")
        print("- Productos más comprados:")
        print(productos_mas_comprados)
        print(f"- Valor medio de las compras: {valor_medio_compras}")

    def productos_mas_vendidos_por_fecha(df, fecha_inicio, fecha_fin):
        # Filtrar el DataFrame por el rango de fechas especificado
        df_filtrado = df[(df['FechaRegistro'] >= fecha_inicio) & (df['FechaRegistro'] <= fecha_fin)]

        # Obtener los productos más vendidos en el rango de fechas especificado
        productos_mas_vendidos = df_filtrado['CodigoArticulo'].value_counts().head(10)

        # Graficar los productos más vendidos en el rango de fechas especificado
        plt.figure(figsize=(12, 8))
        productos_mas_vendidos.plot(kind='bar', color='skyblue')
        plt.ylabel('Cantidad')
        plt.xlabel('Código de Producto')
        plt.title('Top 10 de Productos más vendidos por fecha de registro\n({} - {})'.format(fecha_inicio, fecha_fin))
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        for i, v in enumerate(productos_mas_vendidos):
            plt.text(i, v + 5, str(v), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

        return productos_mas_vendidos

    def graficar_top_clientes(df, columna_pedidos):
    # Calcular el número de pedidos por cliente
        pedidos_por_cliente_10 = df.groupby('CodigodelCliente').size()

    # Excluir el cliente en la posición superior y seleccionar del top 2 al 10
        top_10_clientes = pedidos_por_cliente_10.sort_values(ascending=False).iloc[1:11]

    # Calcular el total de pedidos
        total_pedidos = top_10_clientes.sum()

    # Crear el gráfico de barras con tonos azulados
        plt.figure(figsize=(12, 8))
        colors = plt.cm.Blues(np.linspace(0.3, 1, 10))  # Tonos azulados
        top_10_clientes.plot(kind='bar', color=colors)

    # Mostrar el número absoluto de pedidos en cada barra
        for i, v in enumerate(top_10_clientes):
            plt.text(i, v + 5, str(v), ha='center', va='bottom')

    # Calcular y mostrar el porcentaje de pedidos en cada barra 
        for i, v in enumerate(top_10_clientes):
            porcentaje = (v / total_pedidos) * 100
            plt.text(i, v / 2, f'{porcentaje:.2f}%', ha='center', va='center', color='black')

    # Configurar el título y etiquetas de los ejes
        plt.title('Clientes del 2 al 10 con más pedidos')
        plt.xlabel('Código de Cliente')
        plt.ylabel('Cantidad de Pedidos')

    # Mostrar el gráfico
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def graficar_artic_top_10(df):
        # Obtener la distribución de valores en la columna 'CodigoArticulo'
        distribucion_codigo_articulo = df['CodigoArticulo'].value_counts().head(10)

        # Definir una paleta de colores personalizada
        colores = sns.color_palette("Blues", 10)

        # Crear el gráfico de torta
        plt.figure(figsize=(10, 8))
        distribucion_codigo_articulo.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=colores)

        # Agregar etiquetas a cada sector
        plt.gca().set_aspect('equal')  # Aspecto igual para que la torta sea circular
        plt.legend(distribucion_codigo_articulo.index, loc='best', bbox_to_anchor=(1.3, 0.5))
        plt.title('Top 10 de Códigos de Artículo más Frecuentes')

        # Mostrar el gráfico
        plt.show()

        # Imprimir los top 10 códigos de artículo con su cantidad correspondiente
        print("Top 10 de Códigos de Artículo más Frecuentes:")
        for codigo, cantidad in distribucion_codigo_articulo.items():
            print(f"{codigo}: {cantidad}")

    def top_articulos_y_grafico(dataframe, columna_fecha='FechaPedido', columna_articulo='CodigoArticulo', n_top_articulos=20, n_top_meses=6):
    # Convertir la columna de fechas a tipo datetime
        dataframe[columna_fecha] = pd.to_datetime(dataframe[columna_fecha], format='mixed')

    # Obtener los top n artículos más frecuentes
        top_articulos = dataframe[columna_articulo].value_counts().nlargest(n_top_articulos)

    # Filtrar el DataFrame para incluir solo los 20 mejores artículos
        dataframe_filtrado = dataframe[dataframe[columna_articulo].isin(top_articulos.index)]

    # Obtener el total de artículos
        total_articulos = dataframe_filtrado.shape[0]

    # Crear el gráfico de artículos
        fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras para el total de cada producto
        ax1.bar(top_articulos.index, top_articulos.values, color='skyblue', alpha=0.7)
        ax1.set_ylabel('Cantidad', color='skyblue')

    # Añadir cantidad exacta como leyenda
        for i, (articulo, cantidad) in enumerate(top_articulos.items()):
            ax1.text(i, cantidad, str(cantidad), ha='center', va='bottom')

    # Configuraciones adicionales
        ax1.set_title('Top 20 de Artículos más Frecuentes')
        ax1.set_xlabel('Código del Producto')
        ax1.set_xticklabels(top_articulos.index, rotation=45, ha='right')
        ax1.grid(visible=False)

    # Mostrar el gráfico
        plt.tight_layout()
        plt.show()

    # Imprimir la cantidad exacta y el porcentaje de cada mes en el gráfico de meses
        print("Cantidad exacta de cada mes:")
    # Calcular los top 6 meses con más artículos vendidos
        top_meses = dataframe_filtrado.groupby(dataframe_filtrado[columna_fecha].dt.month).size().nlargest(n_top_meses)
        nombre_meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
        for mes, cantidad in top_meses.items():
            print(f"{nombre_meses[mes]}: {cantidad}")

    # Crear el gráfico de meses
        fig2, ax3 = plt.subplots(figsize=(8, 6))
        top_meses.plot(kind='bar', color='lightblue', alpha=0.7)
        ax3.set_ylabel('Cantidad')
        ax3.set_xlabel('Mes')
        ax3.set_title('Top 6 Meses con más Artículos Vendidos')

    # Cambiar los números de los meses por sus nombres correspondientes
        ax3.set_xticklabels([nombre_meses[mes] for mes in top_meses.index], rotation=45, ha='right')

    # Añadir cantidad exacta como texto en el gráfico de meses
        for i, (mes, cantidad) in enumerate(top_meses.items()):
            ax3.text(i, cantidad, str(cantidad), ha='center', va='bottom')

    # Mostrar el gráfico
        plt.tight_layout()
        plt.show()

    def top_20_articulos_por_mes(df, columna_fecha='FechaPedido', columna_articulo='CodigoArticulo'):
    # Convertir la columna de fechas a tipo datetime si aún no lo está
        if df[columna_fecha].dtype != 'datetime64[ns]':
            df[columna_fecha] = pd.to_datetime(df[columna_fecha], errors='coerce')

    # Extraer el año de la fecha
        df['Año'] = df[columna_fecha].dt.year

    # Filtrar el DataFrame para el año deseado
        año = df['Año'].iloc[0]  # Se asume que todos los datos son del mismo año
        df_año = df[df['Año'] == año]

    # Obtener el top 20 de artículos para cada mes
        for mes in range(1, 13):
            df_mes = df_año[df_año[columna_fecha].dt.month == mes]
            top_20_mes = df_mes[columna_articulo].value_counts().head(20)
            print(f"Top 20 de artículos para {mes}/{año}:")
            print(top_20_mes)
            print()



    def graficar_top_articulos_por_familia(df):
        # Obtener las top 10 familias con más artículos
        top_familias = df['CodigoFamilia'].value_counts().head(10).index

        # Filtrar el DataFrame para incluir solo las top 20 familias
        df_top_familias = df[df['CodigoFamilia'].isin(top_familias)]

        # Obtener los 5 artículos más vendidos por cada tipo de familia
        top_articulos_por_familia = df_top_familias.groupby(['CodigoFamilia', 'CodigoArticulo']).size().groupby('CodigoFamilia').nlargest(5).reset_index(level=0, drop=True)

        # Calcular el porcentaje de cada artículo respecto al total de su familia
        porcentaje_por_familia = top_articulos_por_familia.groupby(level=0).apply(lambda x: x / x.sum() * 100)

        # Configurar los gráficos para cada familia
        for familia, porcentajes in porcentaje_por_familia.groupby(level=0):
            # Crear una nueva figura y ejes para cada familia
            fig, ax = plt.subplots(figsize=(10, 6))

            # Graficar los porcentajes de cada artículo para la familia actual
            porcentajes.plot(kind='bar', stacked=True, ax=ax, color='steelblue')

            # Agregar el porcentaje en cada columna
            for p in ax.patches:
                ax.annotate(f"{p.get_height():.2f}%", (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

            # Configuraciones adicionales
            ax.set_title(f'Porcentaje de los 5 artículos más vendidos para la familia {familia}')
            ax.set_xlabel('Código de Artículo')
            ax.set_ylabel('Porcentaje (%)')

            # Mostrar el gráfico
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

            
            
            
    def grafico_subfamilias_mas_comunes_por_familia(df):
        # Agrupar los códigos de familia y contar las subfamilias más comunes para cada familia
        subfamilias_mas_comunes = df.groupby('CodigoFamilia')['CodigoSubfamilia'].value_counts().groupby(level=0).head(1)
    
        # Filtrar las 10 familias más comunes
        familias_mas_comunes = df['CodigoFamilia'].value_counts().head(10).index
    
        # Filtrar las 10 subfamilias más comunes por cada una de las 10 familias más comunes
        subfamilias_mas_comunes = subfamilias_mas_comunes[subfamilias_mas_comunes.index.get_level_values(0).isin(familias_mas_comunes)]
    
        if subfamilias_mas_comunes.empty:
            print("No hay subfamilias con más de una ocurrencia por familia.")
            return
    
        # Crear el gráfico de barras
        plt.figure(figsize=(10, 6))
        ax = subfamilias_mas_comunes.plot(kind='bar', color='skyblue')
        plt.title('Subfamilias más comunes por familia')
        plt.xlabel('Código de Familia - Código de Subfamilia')
        plt.ylabel('Número de Ocurrencias')
        plt.xticks(rotation=45)
    
        # Añadir el total centrado en cada columna del gráfico
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')
    
        total_general = len(df)

        print("Total y porcentaje de las 10 familias más comunes con sus subfamilias más comunes: ")
        for familia in familias_mas_comunes:
            # Filtrar el DataFrame por la familia actual
            df_familia = df[df['CodigoFamilia'] == familia]
    
            # Obtener el total de la familia actual
            total_familia = len(df_familia)
    
            # Si la familia no tiene subfamilias comunes, continuar con la siguiente familia
            if familia not in subfamilias_mas_comunes.index.get_level_values(0):
                continue
    
            # Obtener el total de la subfamilia más común para la familia actual
            subfamilia_total = subfamilias_mas_comunes[familia]
    
            # Calcular el porcentaje de la familia actual con su subfamilia más común
            porcentaje = (total_familia / total_general) * 100
    
            print(f"Familia: {familia}, Subfamilia: {subfamilia_total} Total: {total_familia}, Porcentaje: {porcentaje:.2f}%")
            
        plt.show()    


##descuentos funciones

    def grafico_descuentos_y_articulos(df):
        # Obtener los tres primeros valores más frecuentes en la columna de descuentos
        top_descuentos = df['%Descuento'].value_counts().head(3).index

        for descuento in top_descuentos:
            # Filtrar el DataFrame por el descuento actual
            df_descuento = df[df['%Descuento'] == descuento]

            # Obtener los tres artículos más frecuentes para este descuento
            top_articulos = df_descuento['CodigoArticulo'].value_counts().head(3)

            # Crear el gráfico de barras para los tres artículos más frecuentes
            plt.figure(figsize=(8, 6))
            ax = top_articulos.plot(kind='bar', color='skyblue')
            plt.title(f'Top 3 Artículos más Vendidos con {descuento}% de Descuento')
            plt.xlabel('Código de Artículo')
            plt.ylabel('Número de Ventas')
            plt.xticks(rotation=45)

            # Añadir el número total en cada barra
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

        plt.show()

# comparativa precio / coste
    def grafico_comparativa_precio_coste(df):
        # Copiar el DataFrame para evitar la advertencia SettingWithCopyWarning
        df = df.copy()
    
        # Calcular el beneficio bruto
        df['BeneficioBruto'] = df['Precio'] - df['PrecioCoste']

        # Calcular el beneficio neto (teniendo en cuenta el IVA)
        df['BeneficioNeto'] = df['BeneficioBruto'] - df['TotalIva']

        # Crear un gráfico de barras para la comparativa
        plt.figure(figsize=(10, 6))
        ax = df[['Precio', 'PrecioCoste']].head(10).plot(kind='bar', color=['skyblue', 'orange'])
        plt.title('Comparativa de Precio de Venta y Precio de Coste')
        plt.xlabel('Producto')
        plt.ylabel('Precio (€)')
        plt.xticks(rotation=45)
        plt.legend(['Precio de Venta', 'Precio de Coste'])
    
        # Añadir el número total en cada barra
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')
    
        plt.show()







# Llama a la función para crear el gráfico de comparativa

