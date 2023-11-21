select car_id, round(avg(minus_date), 1) as AVERAGE_DURATION
from (SELECT car_id, end_date - start_date + 1 as minus_date
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY)
group by car_id
having round(avg(minus_date), 1) >= 7
order by 2 desc, 1 desc