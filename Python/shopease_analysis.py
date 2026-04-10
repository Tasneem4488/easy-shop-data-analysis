import pandas as pd

import numpy as np

from sqlalchemy import create_engine

import mysql.connector

# الاتصال بقاعدة البيانات
engine = create_engine(
    "mysql+mysqlconnector://root:1234@localhost/shopease"
)

print("Connected successfully ✅")

query = "select * from orders"
orders_df = pd.read_sql(query, engine)

print(orders_df.head())
print(orders_df.info())
print(orders_df.isnull().sum())
# shipping_date    38
# delivery_date    67


query2 = "select * from order_details"
order_details_df = pd.read_sql(query2, engine)

print(order_details_df.head())
print(order_details_df.info())
print(order_details_df.isnull().sum())

query3 = "select * from customer"
customer_df = pd.read_sql(query3, engine)

print(customer_df.head())
print(customer_df.info())
print(customer_df.isnull().sum())
# customer_id     0
# fullname        0
# email          21


query4 = "select * from product"
product_df = pd.read_sql(query4, engine)

print(product_df.head())
print(product_df.info())
print(product_df.isnull().sum())
# product_id        0
# product_name      0
# quantity_stock    0
# price             0
# category_id       0

query5 = "select * from category"
category_df = pd.read_sql(query5, engine)

print(category_df.head())
print(category_df.info())
print(category_df.isnull().sum())
# category_id      0
# category_name    0

query6 = "select * from payment"
payment_df = pd.read_sql(query6, engine)

print(payment_df.head())
print(payment_df.info())
print(payment_df.isnull().sum())
# pay_id         0
# amountpaid     0
# pay_method     0
# pay_date      27
# order_id       0

query7 = "select * from phone"
customer_phone_df = pd.read_sql(query7, engine)

print(customer_phone_df.head())
print(customer_phone_df.info())
print(customer_phone_df.isnull().sum())
# phone             0
# another_phone    71
# customer_id       0


query8 = "select * from address"
customer_address_df = pd.read_sql(query8, engine)

print(customer_address_df.head())
print(customer_address_df.info())
print(customer_address_df.isnull().sum())
# id              0
# street          0
# city            0
# country        16
# customer_id     0


dim_cus = pd.merge(customer_df, customer_address_df, how= "left", on= "customer_id")
dim_customer = pd.merge(dim_cus, customer_phone_df, how= "left", on= "customer_id")


print(dim_customer.head())
print(dim_customer.isnull().sum())


dim_customer["country"].fillna("Egypt", inplace= True)

print(dim_customer["country"].head())

dim_customer["another_phone"].fillna("no second phone", inplace= True)

print(dim_customer["another_phone"].head())

print(dim_customer.isnull().sum())



dim_product = pd.merge(product_df, category_df, on= "category_id", how= "inner")

print(dim_product.head())
print(dim_product.isnull().sum())


dim_payment = payment_df.drop(["order_id", "pay_date"], axis= 1)

print(dim_payment.head())
print(dim_payment.isnull().sum())


mer = pd.merge(orders_df, payment_df, on= "order_id", how= "left")

dim_date = mer[["order_date", "shipping_date", "delivery_date", "pay_date"]]

dim_date.insert(0, "date_id", range(1, len(dim_date) + 1))

print(dim_date.head())
print(dim_date.isnull().sum())


mer_order = pd.merge(orders_df, order_details_df, on= "order_id", how= "left")
mer_order_date = pd.merge(mer_order, dim_date, on= "order_date", how="left")

print(mer_order_date.head())
print(mer_order_date.isnull().sum())

fact_seles = mer_order_date.drop(["delivery_date_x","order_date","shipping_date_x","delivery_date_y","shipping_date_y","pay_date"], axis= 1)


print(fact_seles.head())
print(fact_seles.isnull().sum())

print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)

dim_date["order_date"] = pd.to_datetime(dim_date["order_date"])
dim_date["delivery_date"] = pd.to_datetime(dim_date["delivery_date"])
dim_date["shipping_date"] = pd.to_datetime(dim_date["shipping_date"])

details_order_date = pd.DataFrame({
    "year": dim_date["order_date"].dt.year,
    "month": dim_date["order_date"].dt.month,
    "day": dim_date["order_date"].dt.day,
    "hour": dim_date["order_date"].dt.hour,
    "weekday_num": dim_date["order_date"].dt.dayofweek,
    "weekday": dim_date["order_date"].dt.day_name(),
    "is_month_start": dim_date["order_date"].dt.is_month_start,
    "is_month_end": dim_date["order_date"].dt.is_month_end
})

dim_date = dim_date.join(details_order_date, how= "inner")

print("DIM DATE")
print(dim_date.head())
print(dim_date.shape)
print(dim_date.isnull().sum())

print("DIM CUSTOMER")
print(dim_customer.head())
print(dim_customer.shape)
print(dim_customer.isnull().sum())

print("DIM PRODUCT")
print(dim_product.head())
print(dim_product.shape)
print(dim_product.isnull().sum())

print("DIM PAYMENT")
print(dim_payment.head())
print(dim_payment.shape)
print(dim_payment.isnull().sum())

print("FACT SALES")
print(fact_seles.head())
print(fact_seles.shape)
print(fact_seles.isnull().sum())

# def total(unit_price, quantity_order):

#     return unit_price * quantity_order


# fact_seles["total"] = total(fact_seles["unit_price"], fact_seles["quantity_order"])

# print(fact_seles.head())

print("$" * 60)

#      المبيعات  Sales
print(sum(fact_seles["total_amount"])) # 2897000.0
print(fact_seles["total_amount"].mean()) # 22114.503816793895
print(max(fact_seles["total_amount"])) # 72000.0
print(min(fact_seles["total_amount"])) # 1500.0

fact_product = pd.merge(fact_seles, dim_product, on= "product_id", how= "inner")

print(fact_product.isnull().sum())

# which product sold the most unit? اكثر المنتجات عليها طلب
print(fact_product.groupby("product_name")["quantity_order"].sum().sort_values(ascending= False))
# product_name
# THE HIGHEST-SELLING PRODUCT 
# Smart Plug               17
# Mechanical Keyboard      15
# Amazon Alexa             13
# THE LOWEST-SELLING PRODUCT
# Sony Soundbar             4
# Philips Home Theater      4
# Lenovo ThinkPad           4
# iphone 15                 4



# which product sold the most revenue? المنتجات التي حققت اكبر عائد
print(fact_product.groupby("product_name").agg({
    "quantity_order": "sum",
    "total_amount": "sum"
})
.sort_values(by="total_amount",ascending= False).reset_index())
   

# Anther way by pivot table
print(pd.pivot_table(fact_product,values=["quantity_order","total_amount"],
                     index="product_name", aggfunc="sum")
                     .sort_values(by="total_amount", ascending= False))

#              product_name  quantity_order  total_amount
#  HIGH REVENUE PRODUCTS
# 0            HP Laptop i7              11      533000.0
# 1              phone case              12      356000.0
# 2        Dell Inspiron i5               7      290000.0
# 3           ipad 10th Gen               7      209000.0
#  LOW REVENUE PRODUCTS
# 15          Sony Soundbar               4       70000.0
# 16   Philips Home Theater               4       23500.0
# 17             Smart Plug              17       18000.0
# 18    Mechanical Keyboard              15       15500.0

################################################################
#### NOTE: Smart Plug and Mechanical Keyboard
#### low revenue but it is high selling
################################################################

print("$" * 60)

product_stock = fact_product.groupby("product_name").agg({
    "quantity_order": "sum",
    "quantity_stock": "first"
}).sort_values(by="quantity_stock",ascending= False).reset_index()

product_stock["remain_stock"] = product_stock["quantity_stock"] - product_stock["quantity_order"]

print(product_stock)
#              product_name  quantity_order  quantity_stock  remain_stock
# 0             USB_C cable               8              50            42
# 1        screen protector               6              50            44
# 2              phone case              12              30            18
# 3        wireless earbuds              12              20             8
# 4           redmi note 13               8              20            12
# 5              Smart Plug              17              20             3
# 6   JBL Bluetooth Speaker              12              20             8
# 7              power bank               9              15             6
# 8   huawei tablet matepad               6              15             9
# 9     Mechanical Keyboard              15              15             0
# 10          Sony Soundbar               4              12             8
# 11            samsung s23              12              12             0
# 12          ipad 10th Gen               7              10             3
# 13           Amazon Alexa              13              10            -3
# 14           HP Laptop i7              11              10            -1
# 15       Dell Inspiron i5               7               8             1
# 16        Lenovo ThinkPad               4               7             3
# 17   Philips Home Theater               4               5             1
# 18              iphone 15               4               5             1

#######################################################
### NOTE: screen protector  and USB_C cable
### Products with little demand and many in stock
#######################################################

print(product_stock.query("remain_stock <= 5"))
## PRODUCTS AT RISK OF ACCESS   منتجات بخطر النفاذ 
#             product_name  quantity_order  quantity_stock  remain_stock
# 5             Smart Plug              17              20             3
# 9    Mechanical Keyboard              15              15             0
# 11           samsung s23              12              12             0
# 12         ipad 10th Gen               7              10             3
# 13          Amazon Alexa              13              10            -3
# 14          HP Laptop i7              11              10            -1
# 15      Dell Inspiron i5               7               8             1
# 16       Lenovo ThinkPad               4               7             3
# 17  Philips Home Theater               4               5             1
# 18             iphone 15               4               5             1

################################################
## NOTE: HP Laptop i7 and Amazon Alexa 
## products ordered that are not in stock
################################################

print("$" * 60)

category_product_quantity = fact_product.groupby(["category_name","product_name"])["quantity_stock"].first().reset_index()
print(category_product_quantity)

category_quantity = category_product_quantity.groupby("category_name")["quantity_stock"].sum().reset_index()
print(category_quantity)

category_details = (fact_product.groupby("category_name").agg({
    "quantity_order": "sum",
    "total_amount": "sum"
}).sort_values(by="total_amount",ascending= False).reset_index())

category_details["quantity_stock"] = category_quantity["quantity_stock"]

category_details["remain_stock"] = category_details["quantity_stock"]- category_details["quantity_order"]

category_details= category_details[["category_name","quantity_order","quantity_stock","remain_stock","total_amount"]]

print(category_details)

#     category_name  quantity_order  quantity_stock  remain_stock  total_amount
# 0       computers              37              37             0      975500.0
# 1     accessories              47             165           118      858000.0
# 2  mobile devices              37              40             3      701500.0
# 3      smart home              30              62            32      188500.0
# 4      TV & audio              20              30            10      173500.0

################################################################################################
## NOTE: computers and mobile devices ==> out of stock
## accessories demand is high but quantity of stock is large الطلب عالي بس كمية المخزن كبيرة
## TV & audio demand and revenue are low  الطلب و الايرادات قليله
################################################################################################

print("$" * 80)
print("$" * 80)
print("$" * 80)

fact_customer = pd.merge(fact_seles,dim_customer,how= "inner", on= "customer_id")

print(fact_customer.head())
print(fact_customer.isnull().sum())

pivot = pd.pivot_table(fact_customer,values= "total_amount",index="fullname",
                       aggfunc=["sum","max"])

print(pivot)


customer_analysis = fact_customer.groupby("fullname").agg({
    "quantity_order": "sum",
    "total_amount": "sum"
}).sort_values(by="total_amount",ascending=False).reset_index()


print(customer_analysis)

cust_VIP = customer_analysis.query("total_amount > 100000")
cust_mediun = customer_analysis.query("total_amount < 100000 and total_amount > 50000")
cust_low = customer_analysis.query("total_amount < 50000")

print("*" * 50)
print(cust_VIP)

#             fullname  quantity_order  total_amount
# 0         Aimil Reck               2      144000.0
# 1        Chadd Ginie               2      144000.0
# 2      Jayme Parnham               2      144000.0
# 3  Nicolas Parsonson               2      144000.0
# 4          Lee Heitz               2      144000.0
# 5     Karlyn Medford               2      144000.0

print("*" * 50)
print(cust_mediun)
print("*" * 50)
print(cust_low)


print(customer_analysis.query("quantity_order > 2"))

###########################################################################
### NOTE:  all customer_VIP ==> quantity order = 2
###  BUT total amount is high = 144000
### some customer_low and customer_medium 
### has high quantity order [3,4,5] 
###########################################################################

city_performance = fact_customer.groupby("city").agg({
    "total_amount" : "sum",
    "customer_id" : "nunique"
}).sort_values(by="customer_id",ascending= False).reset_index()

print(city_performance)

#        city  total_amount  customer_id
# 0     Cairo      741500.0           35
# 1      Giza     1158500.0           27
# 2      Alex      397000.0           19
# 3     Banha      528000.0           16
# 4  Mansoura       35000.0            1
# 5      Suez       37000.0            1


city_performance["avg_spending"] = city_performance["total_amount"] / city_performance["customer_id"]
city_performance["avg_spending"] =city_performance["avg_spending"].round(2)
city_performance =city_performance.sort_values(by="avg_spending",ascending=False)

print(city_performance)

#        city  total_amount  customer_id  avg_spending
# 1      Giza     1158500.0           27      42907.41
# 5      Suez       37000.0            1      37000.00
# 4  Mansoura       35000.0            1      35000.00
# 3     Banha      528000.0           16      33000.00
# 0     Cairo      741500.0           35      21185.71
# 2      Alex      397000.0           19      20894.74

########################################################################
### NOTE: the city has much customers ===>  Cairo
### BUT the city has high total amount ===> Giza
### the highest average spending is Giza
### advice: we need to increase the number of customer in
### Suez and Mansoura
########################################################################

fact_date = pd.merge(fact_seles,dim_date, on="date_id",how="inner")

print(fact_date.head())
print(fact_date.isnull().sum())












