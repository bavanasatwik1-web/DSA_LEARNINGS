# Write your MySQL query statement below
select e.unique_id,em.name from Employees em
left join EmployeeUni e
on e.id=em.id;