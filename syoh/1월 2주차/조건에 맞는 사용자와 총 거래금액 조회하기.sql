select u.user_id, u.nickname, b.total_sales
from used_goods_user u,
    (select writer_id, sum(price) as total_sales
    from used_goods_board b
    where status = 'DONE'
    group by writer_id) b
where u.user_id = b.writer_id
and total_sales >= 700000
order by total_sales