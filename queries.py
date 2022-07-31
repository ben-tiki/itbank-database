# para leer la base de datos de sql y generar la tabla de html
import pandas as pd
# conecta a la base de datos de sql
import sqlite3

# se establece la conexion con la base de datos 
con = sqlite3.connect('database/itbank.db', check_same_thread=False) # -> el segundo argumento es para poder leer la base desde main.py

def get_html_table(query) -> str:
    """ Genera una tabla html con los datos de la base de datos """

    # se ejecuta la consulta
    base_de_datos = pd.read_sql_query(query, con)
    
    # se convierte la base de datos a html
    table = base_de_datos.to_html(table_id = "query_table", index=False)

    # se deveuelve la tabla de html generada
    return table
