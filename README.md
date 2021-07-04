# productapp
Aplikasi ini digunakan untuk mengakses database produk diecast mobil, yang terdiri dari beberapa kolom yaitu:

productCode = ID produk <br />
productName = Nama produk <br />
productLine = Tipe produk <br />
productScale = Ukuran/skala produk <br />
productVendor = Produsen produk <br />

Untuk sample datanya bisa diakses di products_data.csv dan ERD dari RDBMS bisa dilihat di 
Aplikasi dibangun dengan menggunakan bahasa pemrograman python, sistem RDBMS (MySQL), serta Flask untuk framework API nya 

# API 1: Get Products
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

# API 2: Get Product by Code
API ini digunakan untuk mengakses data produk berdasarkan kode produk. API ini diakses dengan metode POST dengan request URL sbb: 

http://127.0.0.1:5000/product

contoh inputnya adalah sbb:
{
    "productCode" : "S10_1678"
}

maka outputnya adalah sbb:
{
    "productCode": "S10_1678",
    "productName": "1969 Harley Davidson Ultimate Chopper",
    "productLine": "Motorcycles",
    "productScale": "1:10",
    "productVendor": "Min Lin Diecast"
}
