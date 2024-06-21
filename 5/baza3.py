# baza danych - przechowywanie danych
# sql, nosql
# get, post, put/patch, delete  - http
# select, insert, update, delete  - databse
# read, write, write, delete/dispose - file
# CRUD - create, read, update, delete
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych została podłączona")

    insert = '''
    INSERT INTO hardware (id,name,price) VALUES (1,'Apple',6999);
    '''

    # c.execute(insert)
    # conn.commit()

    # select - get
    select = """
    SELECT * FROM hardware;
    """
    for row in c.execute(select):
        print(row)  # (1, 'Apple', 6999.0)

    # update
    update = """
    UPDATE hardware SET price=8999 WHERE id=1;
    """

    # c.execute(update)
    # conn.commit()

    delete = """
    DELETE FROM hardware WHERE id=1;
    """

    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Błąd podczas podłączania bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte
