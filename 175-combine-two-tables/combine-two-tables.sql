# Write your MySQL query statement below
select p.firstName as firstName,p.lastname as lastName,a.city,a.state from person  as p left join address  as a
on a.personid=p.personid;