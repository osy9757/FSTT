select i.ingredient_type, sum(total_order) as TOTAL_ORDER
from first_half f
    inner join icecream_info i
    on f.flavor = i.flavor
group by i.ingredient_type
