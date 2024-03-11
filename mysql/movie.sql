-- list all databases 
show databases;
-- create datbase 
create database moviedb;
use moviedb;
show tables;
create table movie(
	id int auto_increment primary key,
    title varchar(200) not null unique,
    year varchar(100),
    runtime int,
    language varchar(200) default 'malayalam'
);
desc movie;
-- insert data 
insert into movie(title,year,runtime,language)values('premalu','2024',300,'malayalam');
-- listing all records 
select * from movie;
-- query for selecting all movie
select title from movie;
-- print all malayalam movie name 
select * from movie where language='malayalam';
-- select all movies runtime >120
select *from  movie where runtime >120;
-- select all movies name whose lang !=malyalam
select title from movie where language <>'malayalam'; 
-- update query
-- update movies runtime as 125 whose id=3
update movie set runtime =125 where id=3;
-- aadu jevithom
update movie set title ='aadu jeevithom' where id=2; 
-- delete
delete from movie where id=4; 
-- movie and language
 select title,language from movie;
 -- altering table
 -- add new col rating float with default value 3.5
 alter table movie add column rating float default 3.5;
 update movie set rating=4 where id=1;
-- highest rating
select count(*) from movie;
select max(rating) from movie;
select min(rating) from movie;
-- nested query 
select title from movie where rating=(select max(rating) from movie);
select title from movie where rating=(select min(rating) from movie);
select title from movie where runtime=(select max(runtime) from movie);
-- group by
select language,count(*) from movie group by language;
-- print second largest rating
select title,rating from movie where rating=(select max(rating) from movie where rating <> (select max(rating)from movie));
  select * from movie order by runtime desc;



