# Приложение "Ювелирная мастерская" для некоторой организации.
# БД должна содержать таблицу изделие со следующей структкрой записи:
# ФИО клиента, ФИО мастера, вид изделия, материал

import sqlite3 as sq

# with sq.connect('product.db') as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS face")
#     cur.execute("""CREATE TABLE IF NOT EXISTS face(
#     Client_f_name TEXT NOT NULL,
#     Master_f_name TEXT NOT NULL,
#     Product TEXT NOT NULL,
#     Material TEXT,
#     Cost DECIMAL)
#     """)

def insert():
    data = tuple(input('Введите через запятую фио клиента, мастера, изделие, материал, и стоимость(формат 100.00)\n\n').split(','))

    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO face VALUES(?,?,?,?,?)", [data])
        print(data)





def find_expensive():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM face WHERE Cost>100000")
        result = cur.fetchall()
        print(result)

def find_gold():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM face WHERE Material='gold'")
        result = cur.fetchall()
        print(result)

def find_cross():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM face WHERE Product='ring'")
        result = cur.fetchall()
        print(result)
def delete_izja():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM face WHERE Master_f_name='Izmail Lytz Abramovich'")
        pass
def delete_bracelet():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM face WHERE Product='bracelet'")
        pass
def delete_cheep():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM face WHERE Cost<100000")
        pass

def update_midas():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute('UPDATE face SET Material="gold" WHERE cost>50000')
        pass
def update_cross():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute('UPDATE face SET Master_f_name="Nobodyexpects Thespanish Inquisition" WHERE Product="cross"')
        pass

def update_gip():
    with sq.connect('product.db') as con:
        cur = con.cursor()
        cur.execute('UPDATE face SET Client_f_name="Lete Romale Chavale" WHERE Material="gold"')
        pass
insert()