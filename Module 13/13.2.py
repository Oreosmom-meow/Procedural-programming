import mysql.connector
import json

from flask import Flask,Response

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='0917',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/airport/<ICAO>')
def get_screen_name(ICAO):
        sql = f"Select ident, name, municipality from airport where ident = '{ICAO}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        airport_name = result[1]
        location = result[2]
        response = {
            "ICAO" : ICAO,
            "Name" : airport_name,
            "Location" : location
        }
        return response