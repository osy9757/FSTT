select to_char(b.sales_date,'YYYY') as YEAR,
        to_number(to_char(b.sales_date,'MM')) as MONTH,
        a.gender, 
        count(distinct(a.user_id)) as users
from user_info a,(
    select user_id, sales_date
    from online_sale
    ) b
where a.user_id = b.user_id
group by to_char(b.sales_date,'YYYY'), 
        to_number(to_char(b.sales_date,'MM')),
        a.gender
having gender is not null
order by year,month,gender