import pandas as pd
import os


# Ruta de la carpeta que contiene los archivos CSV
file = 'data/NSE_orginal/'

# Ruta de la carpeta donde guardo los archivos CSV
file_save = 'data/NSE/'

data_csv = [data for data in os.listdir(file) if data.endswith(".csv")]

for data in data_csv:
    # Ruta completa del archivo CSV
    route_csv = os.path.join(file, data)
    
    df = pd.read_csv(route_csv)
    
    df.columns = ['id_entidad', 
                  'ESTADO', 
                  'id_municipio', 
                  'municipio',
                  'id_localidad', 
                  'localidad', 
                  'id_ageb', 
                  'manzana',
                  'AB', 
                  'C+', 
                  'C', 
                  'C-', 
                  'D+', 
                  'D', 
                  'E',
                  'NIVEL PREDOMINANTE', 
                  'VIVIENDAS', 
                  'TAMAÑO DE LOCALIDAD']
    df = df.drop(0)

    df['id_entidad'] = pd.to_numeric(df['id_entidad'], errors='coerce', downcast='integer')
    df['id_municipio'] = pd.to_numeric(df['id_municipio'], errors='coerce', downcast='integer')
    df['id_localidad'] = pd.to_numeric(df['id_localidad'], errors='coerce', downcast='integer')
    df['id_ageb'] = pd.to_numeric(df['id_ageb'], errors='coerce', downcast='integer')
    df['manzana'] = pd.to_numeric(df['manzana'], errors='coerce', downcast='integer')

    ## Generar el id_manzana
    df['id_entidad'] = df['id_entidad'].apply(lambda x: f"{x:02d}")
    df['id_municipio'] = df['id_municipio'].apply(lambda x: f"{x:03d}")
    df['id_localidad'] = df['id_localidad'].apply(lambda x: f"{x:04d}")
    df['manzana'] = df['manzana'].apply(lambda x: f"{x:03d}")

    df['CVEGEO'] = df['id_entidad'] + df['id_municipio'].astype(str) + df['id_localidad'].astype(str) + df['id_ageb'].astype(str) + df['manzana'].astype(str)

    column_id_manzana = df.pop('CVEGEO')
    df.insert(7, 'CVEGEO', column_id_manzana)


    save_df = df[['ESTADO', 'CVEGEO', 'NIVEL PREDOMINANTE']]

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    new_data = f"{data}"
    route_new_csv = os.path.join(file_save, new_data)
    save_df.to_csv(route_new_csv, index=False)