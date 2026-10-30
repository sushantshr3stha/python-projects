import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgress", password = "sushant911", port = "5432")
cur = conn.cursor()

#do something

conn.commit()


cur.close()
conn.close()