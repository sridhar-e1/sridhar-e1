import mysql.connector
#num=input()
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database='mydatabase')

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE TABLE users (ID int AUTO_INCREMENT PRIMARY KEY,NAME varchar(50),PHONENO varchar(30),ADDRESS varchar(255) NOT NULL,USERNAME int,PASSWORD int)")
#mycursor.execute("ALTER TABLE users ADD COLUMN fine int NOT NULL AFTER PASSWORD;")

#mycursor.execute("ALTER TABLE users MODIFY PHONENO varchar(30) ")

sql3 = "INSERT INTO users (NAME,PHONENO,ADDRESS,fine) VALUES (%s,%s,%s,%s)"
val3 = ("saiAshwanth","7339012013" ,"Highway 21",'200')
mycursor.execute(sql3,val3)

mydb.commit()
print(mycursor.lastrowid, "record inserted.")
mycursor.execute("select *from users")
result=mycursor.fetchall()
#print(num)
sql1 = "SELECT * FROM users WHERE ID=%s"
adr=('30',)

mycursor.execute(sql1,adr)

myresult = mycursor.fetchall()

print(len(myresult))
for x in myresult:
  print(x)

