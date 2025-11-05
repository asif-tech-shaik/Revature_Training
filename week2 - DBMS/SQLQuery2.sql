create database RevCompanyDB;

use RevCompanyDb;

create table dept(deptno smallint,dname varchar(3) not null,
constraint pk_deptno primary key(deptno));

create table emp(
empno smallint,
ename varchar(30) not null,
mgr smallint,sal numeric(10,2),
comm numeric(7,2),
deptno smallint
constraint pk_empno primary key(empno)
constraint fk_deptno foreign key(deptno) references dept(deptno)
);

select * from emp;
select * from dept;


insert into dept values (10,'IT'),(20,'HR'),(30,'SAL'),(40,'MKT'),(50,'OP');

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10), 
(1002, 'Bob', 1001, 75000.00, NULL, 20),   
(1003, 'Charlie', 1002, 50000.00, 500.00, 30),
(1004, 'Diana', 1003, 52000.00, 300.00, 30),   
(1005, 'Ethan', 1002, 58000.00, NULL, 40),  
(1006, 'Fiona', 1005, 62000.00, NULL, 50); 

SELECT empno as "Emp Num", ename as "Name" 
from emp;

SELECT empno as "Emp Num", ename as "Name" 
from emp where sal>=60000

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where empno=1004;

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where empno!=1004;

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where empno in (1002,1003,1005);

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where empno not in (1002,1003,1005);

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where sal between 40000 and 55000;

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where ename='bob';

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where ename LIKE '__a%';

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where ename LIKE 'd_a%';

SELECT empno as "Emp Num", ename as "Name" 
from emp 
where empno=1004 or ename like '%h%';

SELECT empno as 'Emp Num', ename as "Name" 
from emp 
where empno=1004 and ename like '%a%';

SELECT empno as "Emp Num", ename as "Name" ,sal as "Salary"
from emp 
where sal>50000
order by sal;

SELECT empno as "Emp Num", ename as "Name" ,sal as "Salary", comm as "Commission"
from emp 
where sal>50000
order by sal desc;

SELECT empno as "Emp Num", ename as "Name" ,sal as "Salary", comm as "Commission"
from emp 
order by comm desc, sal desc;

SELECT count(empno) as "No of employee", 
sum(sal) as "Total salary",
avg(comm) as "average comm",
min(sal) as "least sal",
max(sal) as "Top earner"
from emp;

select * from emp;

SELECT deptno as "Department", sum(sal) as "Salary"
from emp 
group by deptno;

SELECT deptno as "Department", sum(sal) as "Salary"
from emp 
group by deptno
having deptno in (10,30,50);

SELECT deptno as "Department", sum(sal) as "Salary"
from emp 
where deptno in (10,30,50)
group by deptno
having sum(sal) >= 62000
order by sum(sal);

insert into dept values(60,'QC'),(70,'CC');

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1007, 'AAA', 1002, 60000.00, NULL, NULL), 
(1008, 'BB', 1001, 75000.00, NULL, NULL),   
(1009, 'C', 1002, 50000.00, 500.00, NULL);

select e.ename, d.dname, d.deptno
from emp e inner join dept d
on d.deptno=e.deptno ;

select e.ename, d.dname
from emp e left outer join dept d
on d.deptno=e.deptno ;

select e.ename, d.dname
from emp e right outer join dept d
on d.deptno=e.deptno ;

select e.ename, d.dname
from emp e full outer join dept d
on d.deptno=e.deptno ;

