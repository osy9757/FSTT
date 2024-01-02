select b.category, sum(s.sales)
from book b
inner join book_sales s
    on b.book_id = s.book_id
where to_char(s.sales_date,'YYYY-MM') = '2022-01'
group by category
order by category