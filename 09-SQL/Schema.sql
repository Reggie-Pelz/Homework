Drop Table If Exists employees;
Drop Table If Exists salaries;
Drop Table If Exists titles;
Drop Table If Exists departments;
Drop Table If Exists department_manager;
Drop Table If Exists department_employee;



CREATE TABLE Employees (
    EmployeeNumber integer Not Null,
    TitleID varchar(30) Not Null,
    Birthdate varchar(10),
    FirstName varchar(30) Not Null,
	LastName varchar(30) Not Null,
	Sex char,
	HireDate varchar(10) Not Null,
	Primary Key(EmployeeNumber)
);


CREATE TABLE Salaries (
    EmployeeNumber integer Not Null,
    Salary varchar(30) Not Null,
	Primary Key(EmployeeNumber)
);


CREATE TABLE Titles (
    TitleID varchar(30) Not Null,
    Title varchar(30) Not Null,
	Primary key(TitleID)
);


CREATE TABLE Departments (
    DepartmentNumber varchar(30) Not Null,
    DepartmentName varchar(30) Not Null,
    Primary Key(DepartmentNumber)
);


CREATE TABLE Department_Manager (
    DepartmentNumber varchar(30) Not Null,
    EmployeeNumber integer Not Null,
    Foreign Key(EmployeeNumber) References Employees(EmployeeNumber),
	Foreign Key(DepartmentNumber) References Departments(DepartmentNumber)
);


CREATE TABLE Department_Employee (
    EmployeeNumber integer Not Null,
    DepartmentNumber varchar(30) Not Null,
	Foreign Key(EmployeeNumber) References Employees(EmployeeNumber),
	Foreign Key(DepartmentNumber) References Departments(DepartmentNumber)
);

select * from titles;