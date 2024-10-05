from db.models.user import Database


db= Database()
db.create_connection()
#db.create_tables()


def get_user(email):
    try:
        db.cursor.execute(
            "SELECT * FROM auth_user WHERE email= %s",
           ( email,))
        user= db.cursor.fetchone()
        return user
    except  Exception as error:
        print(f"Error retrieving data: {error}")
    return None
