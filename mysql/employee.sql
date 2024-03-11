create database employee;
use employee;
create table emp(
	id int auto_increment primary key,
    emp_name varchar(200) not null,
    department varchar(100),
    salary int,
    location varchar(200)
);
show tables;
desc emp;
insert into emp(emp_name,department,salary,location)values
	('anji','hr',50000,'kochi'),('merin','hr',40000,'tvm'),
    ('devu','it',35000,'kochi'),('alphons','it',30000,'tvm'),
    ('abhirami','manager',60000,'pala'),('neethu','accountant',20000,'aluva');
select * from emp;
select emp_name from emp;
select emp_name,department from emp;
select emp_name,department from emp where department='it';
select emp_name,department from emp where department <>'it';
update emp set location='kottayam' where id=2;
delete from emp where id=4;
