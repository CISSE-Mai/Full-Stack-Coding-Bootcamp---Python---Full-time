import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'Hollywood'
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
query = "SELECT * FROM actors LIMIT 20;"
cursor.execute(query)
results = cursor.fetchall()
print(results)