select substr(product_code,0,2) as category, count(product_id) as products
from product 
group by substr(product_code,0,2)
order by category
