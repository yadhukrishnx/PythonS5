import mysql.connector as mc
mydb=mc.connect(host="localhost",user="yadhu",password="password")
mycursor=mydb.cursor()
mycursor.execute("Show databases")
for x in mycursor:
    print(x)
print("\n\n")
mycursor.execute("use yadhukrishna")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
print("\n")
mycursor.execute("select * from department")
for x in mycursor:
    print(x)
print("\n")
mycursor.execute()
mycursor.execute("select * from department")
for x in mycursor:
    print(x)
print(mydb)