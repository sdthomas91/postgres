import psycopg2

#connect to "chinook" database 
connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

#Query 1 - select all recors from the "artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the name column from artist table
# cursor.execute('SELECT "name" FROM "artist"') 

# Query 3 - select only the name column from artist table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"]) 

# Query 4 - select only the name column from artist table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51]) 

# Query 5 - select only the name column from artist table
cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51]) 


#fetch the results (multiple)
results = cursor.fetchall()

#fetch the result (single)
# results = cursor.fetchone()

#close the connection
connection.close()

#print results 
for result in results:
    print(result)

