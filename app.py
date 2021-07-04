from products import database
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def main():
    return "Welcome!"

@app.route("/products")
def showProducts():
    dbresult = mysqldb.showProducts()
    result = []
    for items in dbresult:
        product = {
            "productCode" : items[0],
            "productName" : items[1],
            "productLine" : items[2],
            "productScale" : items[3],
            "productVendor" : items[4]            
        }
        result.append(product)
        
    return jsonify(result)



@app.route("/product", methods=["POST"])
def showProduct():
    params = request.json
    dbresult = mysqldb.showProductByCode(**params)
    product = {
        "productCode" : dbresult[0],
        "productName" : dbresult[1],
        "productLine" : dbresult[2],
        "productScale" : dbresult[3],
        "productVendor" : dbresult[4]            
    }
        
    return jsonify(product)    

@app.route("/insertproduct", methods=["POST"])
def insertProduct():
    params = request.json
    dbresult = mysqldb.insertProduct(**params)
 
    return dbresult  	

@app.route("/updateproduct", methods=["POST"])
def updateProduct():
    params = request.json
    dbresult = mysqldb.updateProductByCode(**params)
 
    return dbresult  

@app.route("/deleteproduct", methods=["POST"])
def deleteProduct():
    params = request.json
    dbresult = mysqldb.deleteProductByCode(**params)
 
    return dbresult  	
	
if __name__ == "__main__":
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')
    
    app.run(debug=True)
    
    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()