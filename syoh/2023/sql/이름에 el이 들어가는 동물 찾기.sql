select animal_id, name
from animal_ins
where animal_type = 'Dog'and lower(name) like '%el%'
order by name