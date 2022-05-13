import sqlite3

sqlite = sqlite3.connect('learn.db')
cursor = sqlite.cursor()
users = cursor.execute("select id, name, password, age from users")
for user in users.fetchall():
    print("id=%d,name=%s,password=%s,age=%d" % (user[0], user[1], user[2], user[3]))
