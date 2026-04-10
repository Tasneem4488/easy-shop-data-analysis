create table order_details(
order_id int,
product_id varchar(4),
quantity_order int,
unit_price decimal(10,2),
primary key (order_id, product_id),
foreign key (order_id) references orders(order_id),
foreign key (product_id) references product(product_id)
)