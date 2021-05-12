from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = '123456'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            email = request.form['username']
            password = request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM logininfo WHERE email=%s AND password=%s", (email, password))
            info = cursor.fetchone()
            print (info)
            if  info is not None:
                if info['email'] == email and info['password'] == password:
                    msg = 'Log in was successful !'
                    return redirect(url_for('index'))
            else:
                return ('For Already existing account: Incorrect username / password! ' \
                       'New here? please register!')


    return render_template('login.html', msg=msg)

@app.route('/new', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO login.logininfo(name, email, password)VALUES(%s,%s,%s)", (username, email, password))
            mysql.connection.commit()
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
