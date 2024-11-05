
import os
import psycopg2
from passlib.context import CryptContext
from db.config.db import Connection

cnn = Connection()
cnn.create_connection()
class Database:

    def __init__(self):
        self.cursor = cnn.cursor
        self.connection = cnn.connection
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
                ('Zel', '12345', 'zel@mail.com', 'user'),
                ('JohnDoe', 'password123', 'johndoe@mail.com', 'user'),
                ('Alice', 'securePass!', 'alice@mail.com', 'admin'),
                ('Bob', 'qwerty', 'bob@mail.com', 'admin'),
                ('Charlie', 'abcde123', 'charlie@mail.com', 'user')
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
    db.create_tables()   
    db.insert_data()   
    db.close()