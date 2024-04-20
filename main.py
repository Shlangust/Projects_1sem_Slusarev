import sqlite3 as sq

with sq.connect('1.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Изделие")
    cur.execute("""CREATE TABLE IF NOT EXISTS Изделие (
    client TEXT NOT NULL,
    master TEXT NOT NULL,
    product TEXT NOT NULL,
    material TEXT,
    price INTEGER
    )""")

# mode = int(input('ввыберете режим : \n1: Ввод\n2: удаление\n3: редактирование\n4: поиск\n'))
# if mode == 1:
#     inp = input('введите через пробел ФИО клиента, ФИО мастера, изделие, товар, материал и цену ').split()
#     with sq.connect('1.db') as con:
#         cur = con.cursor()
#         cur.execute(f"INSERT INTO Изделие (client, master, product, material, price) VALUES ({inp})")

inp = input('введите через пробел ФИО клиента, ФИО мастера, изделие, товар, материал и цену ').split()
try:
    inp[4] = int(inp[4])
except:
    True

print(inp)
with sq.connect('1.db') as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO Изделие (client, master, product, material, price) VALUES ({inp})")