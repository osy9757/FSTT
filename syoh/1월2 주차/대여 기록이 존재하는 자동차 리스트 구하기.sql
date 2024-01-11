select b.car_id
from car_rental_company_car a,(
    select car_id
    from car_rental_company_rental_history
    where to_char(start_date,'YYYY-MM') = '2022-10'
    ) b
where a.car_id = b.car_id
and a.car_type = '세단'
group by b.car_id
order by b.car_id desc