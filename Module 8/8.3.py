import mysql.connector
from geopy import distance

def get_distance(code):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{code}' "
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            coordinates = (row[0], row[1])
    return coordinates

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='****',
         autocommit=True
         )

user_input1 = input("Enter a first ICAO code: ")
location_1 = get_distance(user_input1)
user_input2 = input("Enter a second ICAO code: ")
location_2 =  get_distance(user_input2)
result = distance.distance(location_1, location_2).km
print(f"The distance between {user_input1} and {user_input2} is {result:.2f} km.")
