-- عرض كل العملاء مع طلباتهم و العملاء من غير طلبات
select customer.customer_id, orders.order_date, orders.total_amount,
 orders.status_order, customer.fullname 
from customer left join orders 
on customer.customer_id = orders.customer_id
order by total_amount desc;

-- عرض كل طلب مع المنتجات الموجوده فيه و الكمية و سعر الوحده
select orders.order_id,  order_details.quantity_order, order_details.unit_price,
orders.total_amount, orders.status_order
from orders inner join order_details
on order_details.order_id = orders.order_id
order by total_amount;

-- عرض كل المنتجات مع بياتات الموردين اللي بيوردوها و السعر ومده التوريد
select supplier.supplier_id, supplier.supplier_name, product.product_id,
product.product_name, supplier_product.supplier_price, supplier_product.leadtime
from ((supplier inner join supplier_product 
on supplier.supplier_id = supplier_product.supplier_id)
inner join product on product.product_id = supplier_product.product_id)
order by supplier_name; 




