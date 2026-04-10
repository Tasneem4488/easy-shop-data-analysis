create table payment(
pay_id int primary key auto_increment,
amountpaid decimal(10,2),
pay_method enum('creditcard','paypal','bank','cash') default 'creditcard',
pay_date datetime,
order_id int unique,
foreign key (order_id) references orders(order_id)
);