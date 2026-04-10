INSERT INTO orders (order_id, status_order, order_date, shipping_date, delivery_date, total_amount, customer_id)
VALUES
(1, 'delivered', '2025-10-01', '2025-10-03', '2025-10-05', 40000.00, 122),
(2, 'shipped',   '2025-10-02', '2025-10-04', NULL, 20000.00, 133),
(3, 'pending',   '2025-10-05', NULL, NULL, 15000.00, 144),
(4, 'delivered', '2025-10-03', '2025-10-05', '2025-10-08', 30000.00, 155),
(5, 'canceled',  '2025-10-06', NULL, NULL, 15000.00, 166),
(6, 'delivered', '2025-10-07', '2025-10-09', '2025-10-10', 7000.00, 177),
(7, 'shipped',   '2025-10-08', '2025-10-10', NULL, 35000.00, 188),
(8, 'pending',   '2025-10-09', NULL, NULL, 37000.00, 199),
(9, 'delivered', '2025-10-10', '2025-10-12', '2025-10-15', 2500.00, 1000),
(10, 'pending',  '2025-10-11', NULL, NULL, 1500.00, 1011);

