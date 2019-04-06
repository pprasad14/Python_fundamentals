#CRUD operations
#Create Read Update Delete


import MySQLdb

hostname = "localhost"
username = "root"
password = "MySqlp@ssw0rd"
database = "patient_data"

#open database connection
db = MySQLdb.connect(hostname, username, password, database)

#preparing a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

cursor.execute("SHOW TABLES;")

data = cursor.fetchall()

#to see all tables;
for d in data:
    print(d)
#######

#creating sql statement to execute

sql = ''' CREATE TABLE TEST (
FNAME CHAR(20) NOT NULL,
LNAME CHAR(20),
AGE INT,
GENDER CHAR(1),
INCOME FLOAT) '''

cursor.execute(sql)

######
#inserting values into test table
fnames = ['Alice','Bob','Cathy','Danny']
lnames = ['John','Jack','McGrady','Boyle']
age = [23,32,43,52]
gender = ['F','M','F','M']
income = [1200, 2300, 3200, 2400]

for i in range(len(fnames)):
    sql1 = '''INSERT INTO TEST(FNAME, LNAME, AGE, GENDER, INCOME)
        VALUES ('{}','{}',{},'{}',{});'''.format(fnames[i], lnames[i], age[i], gender[i], income[i])
#    print(sql1)
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
    
#######3
#selecting rows
        
sql2 = "SELECT * from TEST where AGE > 20"

try:
    cursor.execute(sql2)
    results = cursor.fetchall()
    
    for result in results:
        fn = result[0]
        ln = result[1]
        a = result[2]
        g = result[3]
        i = result[4]
        
        print("Fname = {0}, Lname = {1}, Age = {2}, Gender = {3}, Income = {4}".format(fn,ln,a,g,i))
        
except:
    print("Value Fetch error!")


###########

# Update
    
sql3 = "UPDATE TEST SET INCOME = 5000 WHERE GENDER = 'F'"

try:
    cursor.execute(sql3)
    db.commit()
    print("Change successful!")
except:
    db.rollback()
    
    
#######

# Delete 
    
sql4 = "DELETE FROM TEST WHERE AGE IN (23,32)"

try:
    cursor.execute(sql4)
    db.commit()
    print("deletion successful!")
except:
    print("deletion unsuccessful!")
    
#to close database connection:
db.close()