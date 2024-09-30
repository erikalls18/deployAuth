import os
import psycopg2
from  psycopg2  import sql, OperationalError


db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = os.getenv('POSTGRES_HOST')
print("These are my envs:", db_host, db_user, db_name, db_password)

try: 
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )

    cur= conn.cursor()
    delete_table = """DROP TABLE auth_user"""
    create_table= """CREATE TABLE IF NOT EXISTS auth_user(
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR (100) UNIQUE NOT NULL,
                    password  VARCHAR (80) NOT NULL,
                    email VARCHAR(80) NOT NULL,
                    rol VARCHAR (20) NOT NULL)"""

    insert_data = [
            ('Zel', '12345', 'zel@mail.com', 'princesa'),
            ('JohnDoe', 'password123', 'johndoe@mail.com', 'usuario'),
            ('Alice', 'securePass!', 'alice@mail.com', 'administrador'),
            ('Bob', 'qwerty', 'bob@mail.com', 'editor'),
            ('Charlie', 'abcde123', 'charlie@mail.com', 'moderador')
        ]
    insert_query = """INSERT INTO auth_user (user_name, password, email, rol) VALUES (%s, %s, %s, %s);"""
    cur.executemany(insert_query, insert_data)

    cur.execute(delete_table)
    cur.execute(create_table)
    cur.execute(insert_data)

    conn.commit()
except OperationalError as e:
    print(f"Error de conexión a la base de datos: {e}")
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
#cur.close()
#conn.close()
