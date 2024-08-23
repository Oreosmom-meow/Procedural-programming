import mysql.connector

def get_airport_number(code):
    sql = f" select iso_country, type from airport where iso_country = '{code}' order by type "
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        small_occ = 0
        medium_occ = 0
        large_occ = 0
        helicopter_occ = 0
        for row in result:
            if row[1] == 'small_airport':
                small_occ += 1
            elif row[1] == 'medium_airport':
                medium_occ += 1
            elif row[1] == 'large_airport':
                large_occ += 1
            elif row[1] == 'heliport':
                helicopter_occ += 1
        print(f"For country code = {code}, there are {small_occ} small airports, {medium_occ} medium airports, {large_occ} large airports, {helicopter_occ} helicopter airports")
    return

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='****',
         autocommit=True
         )

user_input = input("Enter a country code: ")
get_airport_number(user_input)