# Write your MySQL query statement below


select a.name 
from salesperson as a
where  a.sales_id not in (
    select b.sales_id 
    from orders as b 
    left join company as c
    on b.com_id = c.com_id
    where c.name = "RED"

)
