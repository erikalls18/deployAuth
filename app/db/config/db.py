
import os
from passlib.context import CryptContext
import psycopg2

class Connection():

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
            print("Conected to the database")
        except Exception as error:
            print(f"Error al conectar: {error}")


if __name__ == "__main__":
    conection= Connection()         
    conection.create_connection()  