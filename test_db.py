import psycopg2

db_params = {
    'dbname': 'qanaqer_hr',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def insertData(q):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(q)
            connection.commit()

def selectData(q):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(q)
            return cursor.fetchall()

b = input()
a = "SELECT * FROM users where id = " + b 
d = selectData(a)
c = len(d)
print(c)
