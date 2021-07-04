# productapp
Aplikasi ini digunakan untuk mengakses database produk diecast mobil, yang terdiri dari beberapa kolom yaitu:

productCode = ID produk
productName = Nama produk
productLine = Tipe produk
productScale = Ukuran/skala produk
productVendor = Produsen produk

Untuk sample datanya bisa diakses di products_data.csv dan ERD dari RDBMS bisa dilihat di 
Aplikasi dibangun dengan menggunakan bahasa pemrograman python, sistem RDBMS (MySQL), serta Flask untuk framework API nya 

#API 1: Get Products
API ini digunakan untuk mengakses segala produk yang ada di table products. API ini diakses dengan metode GET dengan request URL sbb: 

http://127.0.0.1:5000/products

contoh outputnya adalah:
[
    {
        "productCode": "S10_1678",
        "productName": "1969 Harley Davidson Ultimate Chopper",
        "productLine": "Motorcycles",
        "productScale": "1:10",
        "productVendor": "Min Lin Diecast"
    },
    {
        "productCode": "S10_1949",
        "productName": "1952 Alpine Renault 1300",
        "productLine": "Classic Cars",
        "productScale": "1:10",
        "productVendor": "Classic Metal Creations"
    }
]
