select a.apnt_no, p.pt_name, a.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from appointment a, patient p, doctor d
where p.pt_no = a.pt_no
and d.dr_id = a.mddr_id
and to_char(a.apnt_ymd,'YYYY-MM-DD') = '2022-04-13'
and d.mcdp_cd = 'CS'
and a.apnt_cncl_yn = 'N'
order by a.apnt_ymd