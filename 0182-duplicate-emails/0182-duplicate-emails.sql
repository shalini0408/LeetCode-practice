# Write your MySQL query statement below
select Email from
(
select Email,count(Email) as n
from Person
group by Email
)as cnt
where n>1;