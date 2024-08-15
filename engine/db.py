import sqlite3

con= sqlite3.connect("jarvis.db")

cursor =con.cursor()
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\ProgramData\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\ONENOTE.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'instagram', 'https://www.instagram.com/')"
#cursor.execute(query)
#con.commit()

# testing module
#app_name = "Word 2013"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])
