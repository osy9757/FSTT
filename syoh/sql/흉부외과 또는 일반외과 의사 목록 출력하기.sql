select dr_name, dr_id, mcdp_cd, to_char(hire_ymd, 'yyyy-mm-dd')
from doctor
where mcdp_cd in ('CS','GS')
order by hire_ymd desc, dr_name 