import pandas as pd
import psycopg2

# Configura la conexión con la base de datos PostgreSQL
conn = psycopg2.connect(database="DWH",
                        user="postgres",
                        password="21419446vi",
                        host="localhost")

# Lee la primera hoja del archivo .xls en un dataframe de pandas
df = pd.read_excel("C:\Users\PC\Documents\Hr_data.xlsx", sheet_name=0)

# Obtiene el número de columnas de la primera hoja
num_cols = len(df.columns)

# Crea la tabla dinámicamente utilizando el cursor
cur = conn.cursor()
table_cols = ", ".join(f"columna{i} VARCHAR(255)" for i in range(1, num_cols+1))
cur.execute(f"CREATE TABLE stage_rrhh ({table_cols})")

# Inserta los datos en la tabla de PostgreSQL utilizando el cursor
for index, row in df.iterrows():
    values = ", ".join(f"'{str(val)}'" for val in row.values)
    cur.execute(f"INSERT INTO stage_rrhh VALUES ({values})")

# Confirma los cambios y cierra la conexión
conn.commit()
conn.close()
