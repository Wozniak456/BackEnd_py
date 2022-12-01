import psycopg2
from backEnd_1.configDB import host, user, password, db_name

def db_init():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM users;"""
            )
            users = cursor.fetchall()
            cursor.execute(
                """SELECT * FROM category;"""
            )
            category = cursor.fetchall()
            cursor.execute(
                """SELECT * FROM currency;"""
            )
            currency = cursor.fetchall()
            cursor.execute(
                """SELECT * FROM record;"""
            )
            record = cursor.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
    return users, category, currency, record

