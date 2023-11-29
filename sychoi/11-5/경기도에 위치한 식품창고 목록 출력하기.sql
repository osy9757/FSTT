SELECT warehouse_id, warehouse_name, address, NVL(freezer_yn, 'N') AS freexer_yn
FROM food_warehouse
WHERE address like '%경기도%'
ORDER BY 1