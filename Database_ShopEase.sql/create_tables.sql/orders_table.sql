create table orders(
order_id int primary key auto_increment,
status_order enum('pending','shipped','delivered','canceled') default 'pending',
order_date datetime,
shipping_date datetime,
delivery_date datetime,
total_amount decimal(10,2),
customer_id int,
foreign key (customer_id) references customer(customer_id)
);