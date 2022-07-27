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

    # el template el cual contendra la tabla
    html_template = f"""

                <html lang="en">\n
                <head>\n    
                <meta charset="UTF-8">\n    
                <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    
                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    
                <link rel="stylesheet" href=\'/static/css/main.css\' />\n    
                <title>Document</title>\n
                </head>\n
                <body>\n    
                <div class="header">\n        
                <h1 id = "registro_transacciones">SQL Table viewer</h1>\n        
                <img src="../static/images/itbank_logo.png" alt="logo">\n    
                </div>\n    
                <form method="POST" id="form">\n        
                <label for="">Inserte su query de SQL</label>\n        
                <input type="text" name="tipo_operacion">\n        
                <input id = "button" type="submit" value="Enviar">\n    
                </form>\n    
                <div id=\'mostrar_datos\'>\n
                {table}\n
                </div>\n
                </body>\n
                </html>

            """


    # se escribe el template en un archivo html, dentro de la carpeta templates
    with open("templates/reporte.html", "w", encoding="utf-8") as f:

        f.write(html_template)