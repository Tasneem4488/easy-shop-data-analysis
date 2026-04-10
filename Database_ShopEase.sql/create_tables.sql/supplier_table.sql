create table supplier(
supplier_id int primary key auto_increment,
supplier_name varchar(225) not null,
country varchar(225)
);
create table supplier_phone(
num_id int primary key auto_increment,
phone varchar(20),
phone2 varchar(20),
supplier_id int,
foreign key (supplier_id) references supplier(supplier_id)
);