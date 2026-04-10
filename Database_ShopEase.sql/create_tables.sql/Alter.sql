alter table customer
modify fullname varchar(250) not null;

alter table supplier 
modify country varchar(200) default 'Egypt';

alter table product 
add constraint chk_quantity check (quantity_stock > 0);

alter table order_details
add constraint chk_order check (quantity_order > 0);

alter table orders 
modify shipping_date date;

alter table orders
modify delivery_date date;

alter table payment
modify pay_date date;