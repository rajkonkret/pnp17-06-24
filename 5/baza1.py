# baza danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Błąd podczas podłączania bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte
