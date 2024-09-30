import psycopg2

conn = psycopg2.connect(
    database = "postgres", 
    user = "postgres", 
    host= '10.0.0.173',
    password = "mysecretpassword",
    port = 5432
)
print("Conection sucessfull")
conn.close()