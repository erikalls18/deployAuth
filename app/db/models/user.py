
import os
import psycopg2


class Database:

    def __init__(self):
        # Obtener las variables de entorno
        self.db_user = os.getenv('POSTGRES_USER')
        self.db_password = os.getenv('POSTGRES_PASSWORD')
        self.db_name = os.getenv('POSTGRES_DB')
        self.db_host = os.getenv('POSTGRES_HOST')
        self.connection = None
        self.cursor = None


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

    def create_tables(self):
        try: 
            delete_table = """DROP TABLE IF EXISTS auth_user"""
            
            create_table= """CREATE TABLE IF NOT EXISTS auth_user(
                            user_id SERIAL PRIMARY KEY,
                            user_name VARCHAR (100) UNIQUE NOT NULL,
                            password  VARCHAR (80) NOT NULL,
                            email VARCHAR(80) NOT NULL,
                            rol VARCHAR (20) NOT NULL)"""

            insert_data= '''
                            INSERT INTO auth_user (user_name, password, email, rol) VALUES ('Zel', '12345', 'zel@mail.com', 'princesa');
                            INSERT INTO auth_user (user_name, password, email, rol) VALUES ('JohnDoe', 'password123', 'johndoe@mail.com', 'usuario');
                            INSERT INTO auth_user (user_name, password, email, rol) VALUES ('Alice', 'securePass!', 'alice@mail.com', 'administrador');
                            INSERT INTO auth_user (user_name, password, email, rol) VALUES ('Bob', 'qwerty', 'bob@mail.com', 'editor');
                            INSERT INTO auth_user (user_name, password, email, rol) VALUES ('Charlie', 'abcde123', 'charlie@mail.com', 'moderador');

                            '''
            self.cursor.execute(delete_table)
            self.cursor.execute(create_table)
            self.cursor.execute(insert_data)
            self.connection.commit()
            print("Tables created")
        except Exception as error:
            print(f"Error creating tables: {error}")
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
    db.close()