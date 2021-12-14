from flask import Flask, jsonify
from flask_mysqldb import MySQL

from MySQLdb.cursors import Cursor

from flask_cors import CORS

from config import config

app = Flask(__name__)

conexion = MySQL(app)

CORS(app)

@app.route('/dados/<search>')
def dados(search=''):
    try:
        if(search==''): 
            return jsonify({'mensage': 'Dados não encontrados'}), 200
            
        cursor = conexion.connection.cursor()
        sql = 'SELECT distinct REG_ANS FROM t_dados where REG_ANS like "%' + search + '%"'
        cursor.execute(sql)
        infs = []
        for fila in cursor.fetchall():
            inf={ 'REG_ANS': fila[0] }
            infs.append(inf)
        
        cursor.execute('SELECT count(distinct REG_ANS) FROM t_dados where REG_ANS like "%' + search + '%"')
        a = cursor.fetchall()
        if(a[0][0] == 0):
            return jsonify({'mensage': 'Dados não encontrados'}), 200
        return jsonify({'data': infs,'mensage': 'Sucesso'}), 200
    except Exception as ex:
        return jsonify({'mensage': 'Dados não encontrados'}), 200

def pagina404(error):
    return '<h1>A página não foi encontrada: Error 404<h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina404)
    app.run()