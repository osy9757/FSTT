select to_number(to_char(datetime,'hh24')) as hour, count(*) as count
from animal_outs
where to_char(datetime,'hh24')>=09 and to_char(datetime,'hh24')<=19
group by to_char(datetime,'hh24')
order by to_char(datetime,'hh24')