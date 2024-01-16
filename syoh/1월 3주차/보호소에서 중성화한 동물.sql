select i.animal_id, i.animal_type, i.name
from animal_ins i, (
    select animal_id
    from animal_outs 
    where sex_upon_outcome not like 'Intact%'
) o
where i.sex_upon_intake like 'Intact%'
and i.animal_id = o.animal_id
order by i.animal_id