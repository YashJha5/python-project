import logging
import json
import azure.functions as func
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'celebal-testdb.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'yash@celebal-testdb'
app.config['MYSQL_PASSWORD'] = 'Eric@123'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

def users():
    with app.app_context():
       cur = mysql.connection.cursor()

       resultValue = cur.execute("SELECT * FROM users")
       if resultValue > 0:
           userDetails = cur.fetchall()
           return render_template('users.html',userDetails=userDetails)
def main(req: func.HttpRequest) -> func.HttpResponse:
    v = users()
    return func.HttpResponse(v)


     
