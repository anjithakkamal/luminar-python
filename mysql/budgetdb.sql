create database budgetdb;
use budgetdb;
show tables;
create table transaction(
	id int auto_increment primary key,
    title varchar(200) not null,
    type enum('expense','income')default'expense',
    category enum('food','fuel','shopping','bills','emi','entertainment','miscellanious')default'miscellanious',
    user varchar(200) not null,
    amount int not null,
    created_date timestamp default current_timestamp
);
desc transaction;
alter table transaction add column created_date timestamp default current_timestamp;
insert into transaction(title,type,category,user,amount)values
	('auto charge','expense','bills','hari',50),
    ('tea','expense','food','unni',20),
    ('auto charge','income','entertainment','hari',5000),
    ('tea','income','food','entertainment',2000),
    ('bus fee','expense','bills','appu',30),
    ('shop','expense','bills','sree',250);
insert into transaction(title,type,category,user,amount)values
('auto charge','income','entertainment','hari',5000),
    ('tea','income','food','entertainment',2000);
select * from transaction;
select * from transaction where user='hari';
select type,sum(amount)from transaction group by type;
select type,sum(amount)from transaction where user='hari' group by type;
select category,sum(amount) from transaction where user='hari' group by category;
-- hari bills(2) food(2)
select category,count(*) as catcount from transaction where user='hari' group by category; 
select category,sum(amount) as catsum from transaction where user='hari' group by category order by catsum desc limit 2;
