use RevCompanyDB

select * from emp; 
select * from dept;
update emp set ename='CC' where empno=1009; 

select e.ename as 'Employee', m.ename as 'Manager'
from emp e join emp m
on e.mgr=m.empno;

select e.ename as 'Employee', d.deptno as 'Deptno'
from emp e cross join dept d;

select * 
from emp e cross join dept d;

select ename from emp where deptno=(select deptno from dept where dname='QC');

select ename from emp where sal>(select avg(sal) from emp);

create view vemp as select empno, ename from emp where deptno in (10,20,30);

select * from vemp;
select * from emp;

insert into emp(empno,ename,deptno) values(1110,'XXXX',20);

insert into vemp values(1111,'YYYY',10);

UPDATE vemp SET empno=10000 where empno=1111;
delete from vemp where empno=10000;
drop view vemp;

create nonclustered index ideptno on emp(deptno);

drop index emp.ideptno;
use RevCompanyDB;

create or alter procedure sp_empdata
	@empno int, @ename varchar(20), @deptno int,@sal numeric(10,2)
as 
begin 
	begin transaction
	insert into emp (empno,ename,sal,deptno) values (@empno,@ename,@sal,@deptno)
	update emp set comm=sal*0.1 where empno=@empno
	commit 
	select * from emp
	return 1
end

declare @status int
exec @status =sp_empdata 1018,'shan',20,10000
print @status

create or alter function dbo.EmpInsertion(@empno int,@ename varchar(20))
returns varchar(20)
as
begin
	--insert into emp(empno,ename) values (@empno,@ename)
	return CAST(@empno AS varchar)+'-'+@ename
end

select dbo.EmpInsertion(2000,'gwer') respone

create or alter function avgsal()
returns table
as
return
	select deptno, avg(sal) as avgsal from emp group by deptno;

SELECT 
    t.deptno, 
    t.avgsal
FROM 
    dbo.avgsal() AS t;

select * from avgsal();

create trigger trg_AfterInsertEmp
on emp
After insert
as
Begin 
	print 'New employee record inserted into emp table.';
end

insert into emp(empno,ename) values (1111,'shaik')

select * from emp;