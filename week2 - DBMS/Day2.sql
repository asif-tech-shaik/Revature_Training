use RevTraining;

BEGIN TRANSACTION;

insert into student values(101, 'AAA', 'QWERY', 'BLR',654654);
insert into student values(102, 'BBB', 'SGFDSGY', 'HR',454544);
insert into student values(103, 'CCC', 'SGFDSGY', 'CNH',654654),(104,'ddd','dsxzfd','sdc',547854);

insert into student(srollno,sname,pin) values(105,'EEE',574556);

insert into student(sname,pin,srollno) values('FFF',545555,106);

save transaction level1;
save transaction level2;

update student set addres='BLR' 
where srollno=105;
update student set city='hjghjg' 
where srollno=105;
update student set city='BLR' 
where srollno=105;

rollback transaction level2;

commit transaction;

delete student where srollno=105;

truncate table student;

SELECT * from student;

