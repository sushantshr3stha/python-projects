import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "sushant911", port = "5432")
cur = conn.cursor()

#do something



cur.execute("""CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);

""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES

(1, 'sushant', 18, 'M'),
(2, 'max', 20, 'M'),
(3, 'ben', 18, 'M'),
(4, 'sita', 33, 'F'),
(5, 'reze', 18, 'F');

""")
conn.commit()
cur.close()
conn.close()