SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, TO_CHAR(r.created_date, 'YYYY-MM-dd') as created_date
FROM used_goods_board b INNER JOIN used_goods_reply r on b.board_id = r.board_id
WHERE TO_CHAR(b.created_date, 'YYYY-MM') = '2022-10'
ORDER BY created_date, b.title