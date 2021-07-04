from mysql.connector import connect

class database:
    def __init__(self):
        try:
            self.db = connect(host='localhost',
                              database='test',
                              user='root',
                              password='')
        except Exception as e:
            print(e)
    
    def showProducts(self):
        try:  
            cursor = self.db.cursor()
            query ='''select * from products2'''
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    
    def showProductByCode(self, **params):
        try:
            cursor = self.db.cursor()
            query = '''
                select * 
                from products2 
                where productCode = '{0}';
            '''.format(params["productCode"])
            
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
    
    def insertProduct(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            crud_query = '''insert into products2 ({0}) values {1};'''.format(column, values)
            # print(crud_query)
            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def updateProductByCode(self, **params):
        try:
            productCode = params['productCode']
            values = self.restructureParams(**params['values'])
            crud_query = '''update products2 set {0} where productCode = {1};'''.format(values, productCode)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def deleteProductByCode(self, **params):
        try:
            productCode = params['productCode']
            crud_query = '''delete from products2 where productCode = {0};'''.format(productCode)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def dataCommit(self):
        self.db.commit()
        
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result