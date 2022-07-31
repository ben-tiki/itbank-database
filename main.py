import flask
import sqlite3
from queries import get_html_table

# se crea una instancia de flask
app = flask.Flask(__name__)

# se establece la conexion con la base de datos 
con = sqlite3.connect('database/itbank.db')

# se define la ruta de la pagina principal
@app.route('/', methods=['GET', 'POST'])
def index():

    # se obtiene el query de la pagina
    if flask.request.method == 'POST': 

        # se genera la tabla de html con el input del usuario
        tipo_operacion = str(flask.request.form['sql_query'])


        # se genera el archivo en base al query
        table_data = get_html_table(tipo_operacion)

        # returns the html template
        return flask.render_template('index.html', table_data=table_data, tipo_operacion=tipo_operacion)


    return flask.render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True)