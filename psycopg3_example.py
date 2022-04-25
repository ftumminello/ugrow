import psycopg

with psycopg.connect(conninfo="hostaddr=70.16.131.61 port=5432 dbname=admin user=admin password=admin") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM City")

        for line in cur:
            print(line)