import mysql.connector
mydb=mysql.connector.connect(user='root',
password='123456',
host='localhost',
)
mycursor=mydb.cursor()
mycursor.execute('create database Bank')
def Menu():
print("MAIN MENU")
print("1. Insert Record/Records")
print("2. Display Records as per Account Number")
print(" a. Sorted as per Account Number")
print(" b. Sorted as per Customer Name")
print(" c. Sorted as per Customer Balance")
print("3. Search Record Details as per the account number")
print("4. Update Record")
print("5. Delete Record")
print("6. TransactionsDebit/Withdraw from the account")
print(" a. Debit/Withdraw from the account")
7
8
print(" b. Credit into the account")
print("7. Exit")
def MenuSort():
print(" a. Sorted as per Account Number")
print(" b. Sorted as per Customer Name")
print(" c. Sorted as per Customer Balance")
print(" d. Back")
def MenuTransaction():
print(" a. Debit/Withdraw from the account")
print(" b. Credit into the account")
print(" c. Back")
def Create():
try:
mycursor.execute('create table bank(ACCNO varchar(10),NAME
varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS
varchar(20),CITY varchar(10),COUNTRY varchar(20),BALANCE
integer(15))')
print("Table Created")
Insert()
except:
print("Table Exist")
Insert()
def Insert():
while True: #Loop for accepting records
Acc=input("Enter account no")
Name=input("Enter Name")
8
9
Mob=input("Enter Mobile")
email=input("Enter Email")
Add=input("Enter Address")
City=input("Enter City")
Country=input("Enter Country")
Bal=float(input("Enter Balance"))
Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Cou
ntry.upper(),Bal]
Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
mycursor.execute(Cmd,Rec)
mydb.commit()
ch=input("Do you want to enter more records")
if ch=='N' or ch=='n':
break
def DispSortAcc():
try:
cmd="select * from BANK order by ACCNO"
mycursor.execute(cmd)
S=mycursor.fetchall()
F="%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE
ADDRESS","CITY","COUNTRY","BALANCE"))
print("="*125)
for i in S:
for j in i:
9
10
print("%14s" % j, end=' ')
print()
except:
print("Table doesn't exist")
def DispSortName():
try:
cmd="select * from BANK order by NAME"
mycursor.execute(cmd)
S=mycursor.fetchall()
F="%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE
ADDRESS","CITY","COUNTRY","BALANCE"))
for i in S:
for j in i:
print("%14s" % j, end=' ')
print()
except:
print("Table doesn't exist")
def DispSortBal():
try:
cmd="select * from BANK order by BALANCE"
mycursor.execute(cmd)
S=mycursor.fetchall()
F="%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE
ADDRESS","CITY","COUNTRY","BALANCE"))
10
11
for i in S:
for j in i:
print("%14s" % j, end=' ')
print()
except:
print("Table doesn't exist")
def DispSearchAcc():
try:
cmd="select * from BANK"
mycursor.execute(cmd)
S=mycursor.fetchall()
ch=input("Enter the accountno to be searched")
for i in S:
if i[0]==ch:
F="%15s %15s %15s %15s %15s %15s %15s %15s"
print(F % ("ACCNO","NAME","MOBILE","EMAIL
ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
for j in i:
print('%14s' % j,end=' ')
print()
break
else:
print("Record Not found")
except:
print("Table doesn't exist")
11
12
def Update():
try:
cmd="select * from BANK"
mycursor.execute(cmd)
S=mycursor.fetchall()
A=input("Enter the accound no whose details to be changed")
for i in S:
i=list(i)
if i[0]==A:
ch=input("Change Name(Y/N)")
if ch=='y' or ch=='Y':
i[1]=input("Enter Name")
i[1]=i[1].upper()
ch=input("Change Mobile(Y/N)")
if ch=='y' or ch=='Y':
i[2]=input("Enter Mobile")
ch=input("Change Email(Y/N)")
if ch=='y' or ch=='Y':
i[3]=input("Enter email")
i[3]=i[3].upper()
ch=input("Change Address(Y/N)")
if ch=='y' or ch=='Y':
i[4]=input("Enter Address")
i[4]=i[4].upper()
ch=input("Change city(Y/N)")
12
13
if ch=='y' or ch=='Y':
i[5]=input("Enter City")
i[5]=i[5].upper()
ch=input("Change Country(Y/N)")
if ch=='y' or ch=='Y':
i[6]=input("Enter country")
i[6]=i[6].upper()
ch=input("Change Balance(Y/N)")
if ch=='y' or ch=='Y':
i[7]=float(input("Enter Balance"))
cmd="UPDATE BANK SET
NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s
WHERE ACCNO=%s"
val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
mycursor.execute(cmd,val)
mydb.commit()
print("Account Updated")
break
else:
print("Record not found")
except:
print("No such table")
def Delete():
try:
cmd="select * from BANK"
mycursor.execute(cmd)
13
14
S=mycursor.fetchall()
A=input("Enter the accound no whose details to be changed")
for i in S:
i=list(i)
if i[0]==A:
cmd="delete from bank where accno=%s"
val=(i[0],)
mycursor.execute(cmd,val)
mydb.commit()
print("Account Deleted")
break
else:
print("Record not found")
except:
print("No such Table")
def Debit():
try:
cmd="select * from BANK"
mycursor.execute(cmd)
S=mycursor.fetchall()
print("Please Note that the money can only be debited if min
balance of Rs 5000 exists")
acc=input("Enter the account no from which the money is to
be debited")
for i in S:
i=list(i)
14
15
if i[0]==acc:
Amt=float(input("Enter the amount to be withdrawn"))
if i[7]-Amt>=5000:
i[7]-=Amt
cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
val=(i[7],i[0])
mycursor.execute(cmd,val)
mydb.commit()
print("Amount Debited")
break
else:
print("There must be min balance of Rs 5000")
break
else:
print("Record Not found")
except:
print("Table Doesn't exist")
def Credit():
try:
cmd="select * from BANK"
mycursor.execute(cmd)
S=mycursor.fetchall()
acc=input("Enter the account no from which the money is to
be debited")
for i in S:
15
16
i=list(i)
if i[0]==acc:
Amt=float(input("Enter the amount to be credited"))
i[7]+=Amt
cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
val=(i[7],i[0])
mycursor.execute(cmd,val)
mydb.commit()
print("Amount Credited")
break
else:
print("Record Not found")
except:
print("Table Doesn't exist")
while True:
Menu()
ch=input("Enter your Choice")
if ch==1:
Create()
elif ch==2:
while True:
MenuSort()
ch1=input("Enter choice a/b/c/d")
if ch1 in ‘Aa’:
DispSortAcc()
16
17
elif ch1 in ‘Bb’:
DispSortName()
elif ch1 in ‘cC’:
DispSortBal()
elif ch1 in ‘Dd’:
print("Back to the main menu")
break
else:
print("Invalid choice")
elif ch==3:
DispSearchAcc()
elif ch==4:
Update()
elif ch==5:
Delete()
elif ch==6:
while True:
MenuTransaction()
ch1=input("Enter choice a/b/c")
if ch1 in ‘bB’:
Debit()
elif ch1 in ‘bB’:
Credit()
elif ch1 in ‘cC’:
print("Back to the main menu")
17
18
break
else:
print("Invalid choice")
elif ch==7:
print("Exiting...")
break
else:
print("Wrong Choice Entered")