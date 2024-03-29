CREATE TABLE LMS_MEMBERS   
(  
MEMBER_ID VARCHAR2(255),   
MEMBER_NAME VARCHAR2(255) NOT NULL ,   
CITY VARCHAR2(255),   
DATE_REGISTER DATE NOT NULL ,   
DATE_EXPIRE DATE,   
MEMBERSHIP_STATUS VARCHAR2(255) NOT NULL   
);

Insert into LMS_MEMBERS (MEMBER_ID,MEMBER_NAME,CITY,DATE_REGISTER,DATE_EXPIRE,MEMBERSHIP_STATUS) values ('LM001','Akshay','CHENNAI','12-06-18','26-10-20','Temporary'),('LM002','Jivika','Baroda','17-06-16','16-10-19','permanent'),('LM003','Janavi','Kolkata','1-03-15','16-11-19','permanent'),
('LM004','Kartik','Baroda','17-06-16','18-1-21','permanent'),
('LM005','Namita','Delhi','11-01-11','15-10-15','Temporary'),
('LM006','Jignesh','Indor','18-06-17','16-11-19','permanent'),
('LM007','Gitanjali','Jabalpur','10-08-16','1-10-19','Temporary'),
('LM008','Kedar','Mumbai','11-01-11','14-5-15','permanent'),
('LM009','Renuka','Pune','12-09-17','9-11-21','permanent'),
('LM010','Mayur','Nayanital','1-12-18','19-7-19','Temporary');

SELECT * FROM LMS_MEMBERS;
SELECT * FROM LMS_MEMBERS WHERE MEMBERSHIP_STATUS="permanent";
SELECT MEMBER_ID,MEMBER_NAME FROM LMS_MEMBERS WHERE MEMBERSHIP_STATUS="permanent" AND CITY="Pune";
SELECT MEMBER_ID,MEMBER_NAME FROM LMS_MEMBERS WHERE MEMBERSHIP_STATUS="permanent" OR CITY="Nayanital";
SELECT MEMBER_ID FROM LMS_MEMBERS WHERE not MEMBERSHIP_STATUS="permanent";
SELECT COUNT(MEMBERSHIP_STATUS) FROM LMS_MEMBERS WHERE MEMBERSHIP_STATUS="Temporary";
SELECT COUNT(MEMBER_ID),MEMBERSHIP_STATUS FROM LMS_MEMBERS GROUP BY MEMBERSHIP_STATUS;


CREATE TABLE LMS_BOOKS   
(  
BOOK_ID VARCHAR2(255),   
BOOK_NAME VARCHAR2(255) NOT NULL ,
MEMBER_ID   VARCHAR2(255),
SUPPLIER_ID VARCHAR2(255),
AUTHER VARCHAR2(255),   
PRICE INT    
);

Insert into LMS_BOOKS (BOOK_ID,BOOK_NAME,MEMBER_ID,SUPPLIER_ID,AUTHER,PRICE) values
('B001','C_PROGRAMMING','LM004','BS04','DENIC_RITCHI',250),
('B002','OPERATING SYSTEM','LM009','BS02','Zac Barnett',200),
('B003','APTITUDE','LM005','BS03','R.S.AGRAWAL',350),
('B004','JAVA','LM001','BS04','DENIC_RITCHI',400),
('B005','PYTHON','LM010','BS05','James gosling',550),
('B006','DATA STRUCTURE','LM005','BS01','Richard petty',330);  

SELECT * FROM LMS_BOOKS;
SELECT SUM(PRICE) FROM LMS_BOOKS WHERE PRICE>=400;

SELECT BOOK_NAME,PRICE FROM LMS_MEMBERS AS T1 INNER JOIN LMS_BOOKS AS T2 ON  T1.MEMBER_ID=T2.MEMBER_ID;


CREATE TABLE LMS_SUPPLIERS_DETAILS   
(  
SUPPLIER_ID VARCHAR2(255),   
SUPPLIER_NAME VARCHAR2(255) NOT NULL ,   
ADDRESS VARCHAR2(255),   
CONTACT INT NOT NULL ,   
EMAIL VARCHAR2(255) NOT NULL    
);

Insert into LMS_SUPPLIERS_DETAILS (SUPPLIER_ID,SUPPLIER_NAME,ADDRESS,CONTACT,EMAIL)values ('BS01','Himalaya book SHOPPEE','CHENNAI',9894123555,'sing@yahoo.com'),
('BS02','Atlantic Books','Lucknow',8874123535,'Atlantic@gmail.com'),
('BS03','A&C Black','Hyderabad',8394924585,'A&C@gmail.com'),
('BS04','Marshall Cavendish','Nagpur',9594322505,'Marshall@gmail.com'),
('BS05','Hay House','Jaipur',98090123855,'Hay123@yahoo.com');

SELECT * from LMS_SUPPLIERS_DETAILS;
SELECT SUPPLIER_ID FROM LMS_SUPPLIERS_DETAILS WHERE EMAIL LIKE "%@gmail.com";
DELETE FROM LMS_SUPPLIERS_DETAILS WHERE SUPPLIER_NAME="Marshall Cavendish";
SELECT * from LMS_SUPPLIERS_DETAILS;
