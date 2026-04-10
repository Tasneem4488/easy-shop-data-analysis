-- عرض كل عميل عمل اجمالي شراء كام
select  customer.customer_id,customer.fullname, sum(orders.total_amount) as total
from orders left join customer
on orders.customer_id = customer.customer_id
group by customer_id
order by total desc;

-- عرض كل حاله فيها كام طلب
select count(order_id) as num, status_order from orders
group by status_order 
order by num;

-- عرض كميه المنتجات المباعه
select product.product_name,
sum(order_details.quantity_order) as quantity from product
inner join order_details on order_details.product_id = product.product_id
group by product_name
order by quantity desc;

-- اجمالي المبيعات وتاريخ الدفع
select sum(orders.total_amount) as total, payment.pay_date
from payment right join orders
on orders.order_id = payment.order_id
group by pay_date
order by pay_date;

-- مبيعات شهر 10 
select sum(total_amount), month(order_date) as month_ , year(order_date) as year_
from orders
group by month_ , year_
having  month_ = 10 and year_ = 2025
order by month_;




