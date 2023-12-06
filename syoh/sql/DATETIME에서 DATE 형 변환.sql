select animal_id, name, to_char(datetime,'yyyy-mm-dd')
from animal_ins
order by animal_id