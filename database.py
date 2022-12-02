# pip install mysql-connector-python
import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="foodAdmin",
    password="password",
    database="test"
)
c = mydb.cursor()


#----------------------------------------view Details---------------------------------------------------------------------------------
def view_all_data_emp():
    c.execute('SELECT employee.EmpID, employee.EmpName , employee.Rating, employee.Supervision , employeepriv.AadhaarID , employeepriv.PanNumber, employeepriv.Email,employeepriv.DL from employeepriv  join employee ON employee.EmpID=employeepriv.EmpID;')
    data = c.fetchall()
    return data
def viewempprv():
    c.execute('Select * from EmployeePriv;')
    data=c.fetchall()
    return data
def viewemp():
    c.execute('Select * from Employee;')
    data=c.fetchall()
    return data
def viewdel():
    c.execute('Select * from Delivery;')
    data=c.fetchall()
    return data
def vieword():
    c.execute('Select * from foodorder;')
    data=c.fetchall()
    return data
def view_available_mns():
    c.execute('SELECT * from menunsupply where ItemQnty>3 ;')
    data = c.fetchall()
    return data
def viewallmns():
    c.execute('SELECT * from menunsupply ;')
    data = c.fetchall()
    return data
def view_lesser_mns():
    c.execute('select itemname,itemqnty,reorderstock(itemqnty) as Status from menunsupply;')
    data = c.fetchall()
    return data
def view_empNames():
    c.execute('SELECT EmpName from employee ;')
    data = c.fetchall()
    return data
def viewempid():
    c.execute('Select empid from employee;')
    data=c.fetchall()
    return data
def viewordID():
    c.execute('Select OrdID from foodorder;')
    data=c.fetchall()
    return data
def mnsname():
    c.execute('Select ItemName from MenuNSupply;')
    data=c.fetchall()
    return data

def viewordnum():
    c.execute('Select OrdID from FoodOrder ;')
    data = c.fetchall()
    return data

def viewratingemp():
    c.execute(' select rating, count(rating) as NoOfEmp from employee group by rating;')
    data=c.fetchall()
    return data

def viewnotpriv():
    c.execute('SELECT * FROM Employee WHERE EmpID NOT IN (SELECT EmpID FROM EmployeePriv);')
    data=c.fetchall()
    return data

def viewtrig():
    c.execute('CREATE TRIGGER sumordd AFTER INSERT ON foodorder for each row set @sumordd = @sumordd + 1;')
    mydb.commit()
    c.execute('SET @sumordd = 0;')
    mydb.commit()
    c.execute('select @sumordd;')
    data=c.fetchall()
    return data

def viewproc():
    c.execute('SET @finalamt = 0;')
    mydb.commit()
    c.execute('call sumoford(@finalamt);')
    mydb.commit()
    c.execute('select @finalamt;')
    data=c.fetchall()
    return data

def viewnumordsold():
    #between 12pm to 9pm - number of orders
    c.execute("select CustID,count(ordid)>4 from foodorder where foodtim between '12:00' and '21:00' group by Custid;")
    data=c.fetchall()
    return data

def viewnumords():
    #between 12pm to 9pm - number of orders
    c.execute("select CustID,count(ordid) from foodorder where foodtim between '11:00' and '21:00' group by Custid;")
    data=c.fetchall()
    return data

def final():
    #more than 4 between 12pm to 9pm
    c.execute('select Custid,morethan4(ordid) from foodorder where foodtim between "11:00" and "21:00" ;')
    data=c.fetchall()
    return data

#def viewchange():
    #more than 4 between time
    #s=viewnumords()
    #d=c.execute('Select CustID from {}')
    #a=
    #c.execute('Select * from customer where CustID="{}"'.format(a))
#----------------------------------------Update Details---------------------------------------------------------------------------------
#-------------for employee------------------------
def get_emp(dealer_name):
    c.execute('SELECT * FROM employee WHERE EmpName="{}"'.format(dealer_name))
    data = c.fetchall()
    return data

def quantityfood(item_name):
    c.execute('Select ItemQnty from MenuNSupply where itemname="{}"'.format(item_name))
    data=c.fetchall()
    return data

def pricefood(item_name):
    c.execute('Select Price from MenuNSupply where itemname="{}"'.format(item_name))
    data=c.fetchall()
    return data

def editempdata(newempID,newEmpname,newratingemp,newsupervisionemp,empID,Empname,ratingemp,supervisionemp):
    c.execute("UPDATE Employee SET EmpID=%s, EmpName=%s, Rating=%s, Supervision=%s WHERE "
              "EmpID=%s and EmpName=%s and Rating=%s and Supervision=%s", (newempID,newEmpname,newratingemp,newsupervisionemp,empID,Empname,ratingemp,supervisionemp))
    mydb.commit()
    data = c.fetchall()
    return data
#-------------for Order------------------------
def get_ord(selected_ord):
    c.execute('SELECT * FROM FoodOrder WHERE OrdID="{}"'.format(selected_ord))
    data = c.fetchall()
    return data
def editorddata(newCustID,newOrdID,newFoodD,newFoodStatus,newTotalAmt,newFoodpay,CustID,OrdID,FoodD,FoodStatus,TotalAmt,Foodpay):
    c.execute("UPDATE FoodOrder SET CustID=%s, OrdID=%s, FoodStatus=%s, TotalAmt=%s, Foodpay=%s WHERE "
              "CustID=%s and OrdID=%s and FoodStatus=%s and TotalAmt=%s and Foodpay=%s", (newCustID,newOrdID,newFoodD,newFoodStatus,newTotalAmt,newFoodpay,CustID,OrdID,FoodD,FoodStatus,TotalAmt,Foodpay))
    mydb.commit()
    data = c.fetchall()
    return data
#---------------------------for menu and supply-------------------------------
def get_mns(selected_mns):
    c.execute('SELECT * FROM MenuNSupply WHERE ItemName="{}"'.format(selected_mns))
    data = c.fetchall()
    return data
def editmnsdata(newItemID,newItemName,newItemQnty,newFoodAvailibility,newPrice,ItemID,ItemName,ItemQnty,FoodAvailibility,Price):
    c.execute("UPDATE MenuNSupply SET ItemID=%s, ItemName=%s, ItemQnty=%s, FoodAvailability=%s, Price=%s WHERE "
              "ItemID=%s and ItemName=%s and ItemQnty=%s and FoodAvailability =%s and Price=%s", (newItemID,newItemName,newItemQnty,newFoodAvailibility,newPrice,ItemID,ItemName,ItemQnty,FoodAvailibility,Price))
    mydb.commit()
    data = c.fetchall()
    return data

def getcurtime():
    c.execute("select DATE_FORMAT(now(),'%k:%i');")
    data=c.fetchall()
    return data

#----------------------------------------Insert Details---------------------------------------------------------------------------------
def addordermain(paymentmethod):
    a=getcurtime()
    final=a[0][0]
    c.execute('INSERT INTO foodorder values("C1", null , curdate() ,"{}", null , "{}")'.format(final,paymentmethod))
    mydb.commit()

def getprice(I):
    c.execute('Select Price from MenunSupply where Itemname=%s',I)
    mydb.commit()

def getitemid(I):
    c.execute('Select ItemID from menunsupply where ItemName="{}"'.format(I))
    data=c.fetchall()
    final=data[0][0]
    return final

def addintocustord(a,b):
    #p=getprice(a)
    iid= getitemid(a)
    c.execute('Insert into custord values("C1","{}",{})'.format(iid,b))
    mydb.commit()

def addintomainord(price):
    a=getcurtime()
    final=a[0][0]
    c.execute('UPDATE foodOrder SET Amount={} where foodtim="{}"'.format(price,final))
    mydb.commit()

def addempdata(employeeid,employeename,rating,super):
    c.execute('Insert into employee values ("{}","{}",{},"{}")'.format(employeeid,employeename,rating,super))
    mydb.commit()

def addempdelivery():
    l=viewempid()
    f=random.choice(l)
    c.execute('Insert into Delivery values (null,"C1",now(),"E3");')
    mydb.commit()



#----------------------------------------Delete Details---------------------------------------------------------------------------------
#-------------for employee----------------
#def delete_dataemp(emp_name):
#    c.execute('DELETE FROM Employee WHERE EmpName="{}"'.format(emp_name))
#    mydb.commit()

def delete_dataemp(emp_name):
    c.execute('delete from employeepriv where empID in (select empid from employee where empname="{}")'.format(emp_name))
    mydb.commit()
    #c.execute('Delete from employee where Supervision=')
    c.execute('DELETE FROM Employee WHERE EmpName="{}"'.format(emp_name))
    mydb.commit()

def delete_datamns(ItemName):
    c.execute('DELETE FROM MenuNSupply WHERE ItemName="{}"'.format(ItemName))
    mydb.commit()





