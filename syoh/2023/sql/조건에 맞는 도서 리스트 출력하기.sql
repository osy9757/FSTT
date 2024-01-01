select book_id, published_date
from book
where category = '인문' and to_char(published_date,'YYYY') = '2021'
order by to_char(published_date,'YYYY-MM-DD')