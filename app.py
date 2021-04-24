from MySQLdb.cursors import Cursor
from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL



main = Flask(__name__)

main.config['MYSQL_HOST'] = 'localhost'
main.config['MYSQL_USER'] = 'root'
main.config['MYSQL_PASSWORD'] = ''
main.config['MYSQL_DB'] = 'dbTareas'

mysql = MySQL(main)

@main.route('/')
def index():

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, taskName, description from tasks')
    tareas = cursor.fetchall()
    cursor.close()
    return render_template('index.html', tasks=tareas)

@main.route('/saveTask', methods=['POST'])
def save():
    cursor = mysql.connection.cursor()
    name = request.form['taskName']
    desc = request.form['taskDesc']
    cursor.execute('INSERT INTO tasks (taskName, description) values(%s, %s)', (name, desc))
    mysql.connection.commit()
    cursor.close()
    return redirect('/')

@main.route('/updateTask', methods=['POST'])
def update():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        currentId = request.form['idTask']
        name = request.form['taskName']
        desc = request.form['taskDesc']

        cursor.execute('UPDATE tasks set taskName = %s, description = %s where id = %s', (name, desc, currentId))
        mysql.connection.commit()
        cursor.close()
        return redirect('/')
    else:
        return jsonify(respuesta="Error")

@main.route('/deleteTask/<string:id>')
def delete(id):
    cursor = mysql.connection.cursor()
    deleteId = cursor.execute('DELETE from tasks where id = {0}'.format(id))
    mysql.connection.commit()
    cursor.close()
    return redirect('/')

if __name__ == '__main__':
    main.run(debug=True, port=5000)