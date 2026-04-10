create table supplier_product(
supplier_id int,
product_id varchar(4),
leadtime int,
supplier_price decimal(10,2),
primary key (supplier_id, product_id),
foreign key (supplier_id) references supplier(supplier_id),
foreign key (product_id) references product(product_id)
);