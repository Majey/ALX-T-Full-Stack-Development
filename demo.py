import psycopg2

connection = psycopg2.connect("host=localhost user=postgres password=ICUI4CU1997 dbname=example")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS table2")

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    "id":1,
    "completed": False
}

cursor.execute('''
    CREATE TABLE table2 (
        id SERIAL PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute(SQL, data)
cursor.execute("INSERT INTO table2(id, completed) VALUES(2, False);")
cursor.execute("INSERT INTO table2(id, completed) VALUES(3, True);")

cursor.execute("SELECT * FROM table2;")
#result = cursor.fetchall()
#result = cursor.fetchone()
result = cursor.fetchmany(2)
print(result)

for i in result:
    print(i)

connection.commit()

connection.close()
cursor.close()