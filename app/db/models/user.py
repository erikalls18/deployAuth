
import os
import psycopg2
from passlib.context import CryptContext


class Database:

    def __init__(self):
        # Obtener las variables de entorno
        self.db_user = os.getenv('POSTGRES_USER')
        self.db_password = os.getenv('POSTGRES_PASSWORD')
        self.db_name = os.getenv('POSTGRES_DB')
        self.db_host = os.getenv('POSTGRES_HOST')
        self.connection = None
        self.cursor = None
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host
            )
            self.cursor = self.connection.cursor()
            print("Conectado a la base de datos")
        except Exception as error:
            print(f"Error al conectar: {error}")

    def hash_password(self, password):
        return self.pwd_context.hash(password)

    def create_tables(self):
        try: 
            delete_table = """DROP TABLE IF EXISTS auth_user"""
            
            create_table= """CREATE TABLE IF NOT EXISTS auth_user(
                            user_id SERIAL PRIMARY KEY,
                            user_name VARCHAR (100) UNIQUE NOT NULL,
                            password  VARCHAR (80) NOT NULL,
                            email VARCHAR(80) NOT NULL,
                            rol VARCHAR (20) NOT NULL)"""
            self.cursor.execute(delete_table)
            self.cursor.execute(create_table)
            self.connection.commit() 
            print("Tables created")
        except Exception as error:
            print(f"Error creating tables: {error}")
            
    def insert_data(self):
            
            users = [
                ('Zel', '12345', 'zel@mail.com', 'princesa'),
                ('JohnDoe', 'password123', 'johndoe@mail.com', 'usuario'),
                ('Alice', 'securePass!', 'alice@mail.com', 'administrador'),
                ('Bob', 'qwerty', 'bob@mail.com', 'editor'),
                ('Charlie', 'abcde123', 'charlie@mail.com', 'moderador')
            ]

            for user in users:
                hashed_password = self.hash_password(user[1])
                insert_data = '''
                    INSERT INTO auth_user (user_name, password, email, rol) 
                    VALUES (%s, %s, %s, %s)'''
                self.cursor.execute(insert_data, (user[0], hashed_password, user[2], user[3]))
            self.connection.commit()
            
        
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Closed Conection")

if __name__ == "__main__":
    db = Database()         
    db.create_connection()  
    db.create_tables()   
    db.insert_data()   
    db.close()