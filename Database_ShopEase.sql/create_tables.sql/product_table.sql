create table product(
product_id varchar(4) primary key,
product_name varchar(225),
quantity_stock int,
price decimal(10,2),
category_id int,
foreign key (category_id) references category(category_id)
);