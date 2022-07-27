import psycopg2

connection = psycopg2.connect("dbname=example password=ICUI4CU1997 user=postgres")

# Open a cursor to perform database operations
cursor = connection.cursor()

# drop any existing todo table
cursor.execute("DROP TABLE IF EXISTS todo;")

# (re)create the todo table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
    CREATE TABLE todo(
        id SERIAL PRIMARY KEY,
        description VARCHAR NOT NULL
    );
""")

# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()