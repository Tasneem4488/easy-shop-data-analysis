-- الاستعلام 1 :     عرض جميع العملاء
select * from customer;

-- االاستعلام 2 :      لطلبات فوق  30000
select order_id, total_amount from orders
where total_amount > 30000;

--  الاستعلام 3 :   الطلبات بين تاريخين
select order_id, total_amount, order_date from orders
where order_date between '2025-10-06' and '2025-10-9';
