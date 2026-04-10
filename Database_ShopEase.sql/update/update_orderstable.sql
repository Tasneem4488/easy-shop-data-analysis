UPDATE orders
SET order_date = CONCAT(DATE(order_date), ' 12:00:00')
WHERE order_id BETWEEN 1 AND 10;

