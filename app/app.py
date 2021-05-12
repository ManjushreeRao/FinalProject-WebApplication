from __future__ import print_function
from __future__ import print_function
from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect, json, jsonify
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from google_auth_oauthlib.flow import InstalledAppFlow
import json
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
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/academics/')
def academics():
    return render_template('academics.html')


@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/calendar/')
def calendar():
    return render_template('calendar.html')

@app.route('/covid/')
def covid():
    return render_template('covid.html')


@app.route('/Faculty/')
def Faculty():
    return render_template('Faculty.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def main():
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])


if __name__ == '__main__':
    app.run(debug=True)
