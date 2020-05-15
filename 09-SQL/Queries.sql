-- List the following details of each employee: employee number, last name, first name, gender, and salary.

select employees.employeenumber, employees.lastname, employees.firstname, employees.sex, salaries.salary 
from employees
join salaries
using(employeenumber);



-- List employees who were hired in 1986.

select * from employees
where hiredate like '%1986';


-- List the manager of each department with the following information: department number, department name, the manager's employee number, 
-- last name, first name, and start and end employment dates  (where is ending employment date?).

select departments.departmentnumber, departments.departmentname, employees.employeenumber, employees.lastname, employees.firstname, employees.hiredate
from departments
join department_manager
using(departmentnumber)
join employees
using(employeenumber);


-- List the department of each employee with the following information: employee number, last name, first name, and department name.

select employees.employeenumber, employees.lastname, employees.firstname, departments.departmentname
from employees
join department_employee
using(employeenumber)
join departments
using(departmentnumber);


-- List all employees whose first name is "Hercules" and last names begin with "B."

select * from employees
where firstname = 'Hercules' and lastname like 'B%';


-- List all employees in the Sales department, including their employee number, last name, first name, and department name.

select employees.employeenumber, employees.lastname, employees.firstname, departments.departmentname
from departments
join department_employee
using(departmentnumber)
join employees
using(employeenumber)
where departmentname = 'Sales';


-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select employees.employeenumber, employees.lastname, employees.firstname, departments.departmentname
from departments
join department_employee
using(departmentnumber)
join employees
using(employeenumber)
where departmentname = 'Sales' or departmentname = 'Development';


-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select lastname, count(lastname) from employees
group by lastname
order by count(lastname) desc;

