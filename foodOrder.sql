SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



-----------------------------------------------------------------------------------------------------------------------------------------------

-- ----------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE Customer (
  CustomerID varchar(20) ,
  CustName varchar(30),
  Email varchar(20),
  Phone_Number int(10));

Create TABLE CustomerAddress (
  CustomerID varchar(20),
  Building Varchar(30),
  Road_Number varchar(30),
  City varchar(20),
  CounState varchar(20),
  PinCode varchar(10));

INSERT INTO Customer values ('C1','Namitha Bhandary','namibhandu@gmail.com',9886622561);
INSERT INTO Customer values ('C2','Janani','jananiananthkumar@gmail.com',9902800581);
INSERT INTO Customer values ('C3','Bittu','bittu12@gmail.com',9945534343);
INSERT INTO Customer values ('C4','Piyush','piyush@gmail.com',8907126547);
INSERT INTO Customer values ('C5','Harini Golla','harinigolla17@gmail.com',9780374802);

INSERT INTO CustomerAddress values ('C1','Raghuram Apt','#30','Bangalore','Karnataka','560054');
INSERT INTO CustomerAddress values ('C2','Divya Apt','#3','Bangalore','Karnataka','560053');
INSERT INTO CustomerAddress values ('C3','Sterling Apts','#69','Bangalore','Karnataka','560023');
INSERT INTO CustomerAddress values ('C4','Brigade Apts','#89','Bangalore','Karnataka','560006');
INSERT INTO CustomerAddress values ('C5','Krishna Gardenia','#45','Bangalore','Karnataka','560009');


-- ----------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE Employee (
  EmpID varchar(20),
  EmpName varchar(20),
  Rating int,
  Supervision varchar(20));

INSERT INTO Employee values ('E1','Satish',4.5,'E1');
INSERT INTO Employee values ('E2','Harish',4.2,'E1');
INSERT INTO Employee values ('E3','Naman',4.6,'E2');
INSERT INTO Employee values ('E4','Alwin',4.8,'E2');
INSERT INTO Employee values ('E5','Srujana',4.5,'E2');
INSERT INTO Employee values ('E6','Yuktha',4.5,'E2');
INSERT INTO Employee values ('E7','Prashanth',4.5,'E3');
INSERT INTO Employee values ('E8','Kumar',4.5,'E3');
INSERT INTO Employee values ('E9','Akash',4.5,'E3');
INSERT INTO Employee values ('E10','Nanu',4.7,'E3');


Create table EmployeePriv(
  EmpID varchar(20),
  AadhaarID varchar(30),
  PanNumber varchar(30),
  Email varchar(30),
  DL varchar(30));


INSERT into EmployeePriv values ('E1','3456 5678 6789','356 789','hu@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E2','3456 5678 6789','356 789','huhu@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E3','3456 5678 6789','356 789','hudc@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E4','3456 5678 6789','356 789','hkjdwu@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E5','3456 5678 6789','356 789','hujdj@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E6','3456 5678 6789','356 789','hdjku@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E7','3456 5678 6789','356 789','wndk@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E8','3456 5678 6789','356 789','dcnw@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E9','3456 5678 6789','356 789','dn@gmail.com','KA 89082873891');
INSERT into EmployeePriv values ('E10','3456 5678 6789','356 789','kdjcnw@gmail.com','KA 89082873891');


-----------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE FoodOrder(
  CustID varchar(20),
  OrdID int auto_increment PRIMARY KEY, 
  foodDt date, 
  foodtim varchar(30),
  amount int default null,
  foodpay varchar(20));

create table custord(
  custID varchar(20),
  itemid varchar(20),
  quantity int);
-----------------------------------------------------------------------------------------------------------------------------------------------

create table Delivery(DeliveryID int auto_increment primary key ,Destination varchar(20), FoodDate datetime , EmpID varchar(20));

-- ----------------------------------------------------------------------------------------------------------------------------------------------

create table MenuNSupply(ItemID varchar(20),ItemName varchar(20),ItemQnty int , FoodAvailability varchar(10),Price int);

INSERT into MenuNSupply values('I1','Veggie Paradise Pizza',10,'Y',300);
INSERT into MenuNSupply values('I2','Barbeque Chicken Pizza',3,'Y',400);
INSERT into MenuNSupply values('I3','Margarita Pizza',1,'Y',250);
INSERT into MenuNSupply values('I4','Saucage Paradise Pizza',19,'Y',400);
INSERT into MenuNSupply values('I5','Pesto Pasta',4,'Y',280);
INSERT into MenuNSupply values('I6','Red Sauce Pasta',10,'Y',250);
INSERT into MenuNSupply values('I7','White Sauce Pasta',1,'Y',250);
INSERT into MenuNSupply values('I8','Choco Lava Cake',16,'Y',50);
INSERT into MenuNSupply values('I9','Red Velvet Cake',10,'Y',50);

-- ----------------------------------------------------------------------------------------------------------------------------------------------
-- ----------------------------------------------------------------------------------------------------------------------------------------------

Alter Table MenuNSupply ADD PRIMARY KEY(ItemID);
alter table Employee add primary key(EmpID);
alter table Customer add primary key(CustomerID);

--alter table FoodCustom add Constraint MenuNSupplycons FOREIGN KEY (ItemID) references MenuNSupply(ItemID);
--alter table FoodOrder add Constraint Ordercons FOREIGN KEY CustID references Customer(CustomerID);
--alter table Delivery add Constraint Delicons1 FOREIGN KEY OrdID references FoodOrder(OrdID);
--alter table Delivery add Constraint Delicons2 FOREIGN KEY EmpID references Employee(EmpID);
--alter table Employee add Constraint Empcons FOREIGN KEY Supervision references Employee(EmpID);
--alter table CustomerAddress add Constraint custcons FOREIGN KEY CustomerID references Customer(CustomerID);
--alter table EmployeePriv add Constraint empcons2 FOREIGN KEY EmpID references Employee(EmpID);

ALTER TABLE FoodOrder ADD CONSTRAINT Ordercons FOREIGN KEY (CustID) REFERENCES Customer(CustomerID) on delete cascade; --done
--ALTER TABLE Delivery ADD CONSTRAINT Delicons1 FOREIGN KEY (OrdID) REFERENCES FoodOrder(OrdID) on delete cascade; --done
ALTER TABLE Delivery ADD CONSTRAINT Delicons2 FOREIGN KEY (EmpID) REFERENCES Employee(EmpID) on delete cascade; --done
ALTER TABLE Employee ADD CONSTRAINT Empcons1 FOREIGN KEY (Supervision) REFERENCES  Employee(EmpID) on delete cascade ; -- done
ALTER TABLE EmployeePriv ADD CONSTRAINT Empcons2 FOREIGN KEY (EmpID) REFERENCES  Employee(EmpID) on delete cascade; --done
ALTER TABLE CustomerAddress ADD CONSTRAINT custcons FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) on delete cascade;  --done 
ALTER TABLE custord ADD CONSTRAINT custordcons FOREIGN KEY (custID) REFERENCES Customer(CustomerID) on delete cascade;  --done 

-- functions--------------------------------------------------------

DELIMITER $$ 
CREATE FUNCTION reorderstock(ItemQnty int) 
RETURNS varchar(30)
DETERMINISTIC 
BEGIN 
DECLARE VALUE varchar(30); 
IF ItemQnty>3 then 
set VALUE="Sufficient stock"; 
 ELSE 
set VALUE ="Insufficient stock- REORDER"; 
 end if; 
 return value; 
END;$$ 
DELIMITER ;


DELIMITER $$ 
CREATE FUNCTION morethan4(ordid int) 
RETURNS varchar(30)
DETERMINISTIC 
BEGIN 
DECLARE VALUE varchar(50); 
IF ordid>4 then 
set VALUE="Ordered more than 4 times"; 
 ELSE 
set VALUE ="----"; 
 end if; 
 return value; 
END;$$ 
DELIMITER ;

-- trigger-------------------------------------------------------------
CREATE TRIGGER sumordd AFTER INSERT ON foodorder for each row set @sumordd = @sumordd + 1;
SET @sumord = 0;

--select @sumord;

-- procedure-----------------------------------------------------------
DELIMITER //
CREATE PROCEDURE SumOford (OUT param1 INT)
BEGIN
SELECT SUM(Amount) INTO param1 FROM foodorder;
END;
//
Delimiter ;

--SET @finalamt = 0;
--call sumoford(@finalamt);


-- select @finalamt;

--display details of customer if he has ordered more than 4 times between 12pm to 9pm- function 

COMMIT;
