

class Configuration:
    def __init__(self, database, user, host, password, port):
        self.database = database
        self.user = user
        self.host = host
        self.password = password
        self.port = port

config =Configuration("postgres", "postgres", "10.0.0.173", "mysecretpassword", 5432)

db_params = {
    'dbname': config.database,
    'user': config.user,
    'host': config.host,
    'password': config.password,
    'port': config.port
}