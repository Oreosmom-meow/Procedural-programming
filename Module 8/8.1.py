import mysql.connector

def get_screen_name(number):
    sql = f"Select ident, name, municipality from airport where ident = '{number}'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"For ICAO number: {row[0]}, the airport name is: {row[1]},the municipality is: {row[2]} .")
    return

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='****',
         autocommit=True
         )

user_input = input("Enter a ICAO number: ")
get_screen_name(user_input)
