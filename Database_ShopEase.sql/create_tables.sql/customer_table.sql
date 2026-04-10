create table customer(
customer_id int primary key,
fullname varchar(250),
email varchar(250)
);
create table phone(
phone varchar(20) primary key,
another_phone varchar(20),
customer_id int,
foreign key (customer_id) references customer(customer_id)
);
create table address(
id int primary key auto_increment,
street varchar(200),
city varchar(200),
country varchar(200),
customer_id int,
foreign key (customer_id) references customer(customer_id)
);