select  a.user_id, a.nickname, 
        a.city || ' ' || a.street_address1 || ' ' || a.street_address2 as 전체주소,
        substr(a.tlno,1,3) || '-' || substr(a.tlno,4,4) || '-' || substr(a.tlno,8,4) as 전화번호
from used_goods_user a,
    ( 
        select writer_id, count(*)
        from used_goods_board  
        group by writer_id
        having count(*) >= 3
    ) b
where a.user_id = b.writer_id
order by a.user_id desc