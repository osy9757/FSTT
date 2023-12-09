select count(*)
from user_info
where age>=20 and age<=29 
and to_char(joined,'YYYY') = '2021';