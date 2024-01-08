select history_id as "HISTORY_ID"
    ,car_id as "CAR_ID"
    ,to_char(start_date,'YYYY-MM-DD') as "START_DATE"
    ,to_char(end_date,'YYYY-MM-DD') as "END_DATE"
    ,case when end_date - start_date + 1 >= 30 then '장기 대여'
         else '단기 대여'
    end as "RENT_TYPE"
from car_rental_company_rental_history
where to_char(start_date,'YYYY-MM') = '2022-09'
order by history_id desc