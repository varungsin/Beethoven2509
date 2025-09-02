#  id, name description, category, stock, tags, price
class Product:
    def __init__(self, id, name, description, category, tags, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price
        
    def __str__(self):
        return f'id = {self.id}, name = {self.name},description = {self.description},category = {self.category}, tags = {self.tags}, stock = {self.stock}, price = {self.price}'
    
    def __repr__(self):
        return self.__str__()
    
'''
mobile_OnePlus = Product(1001,'OnePlus 13R','Good camera quality.','mobile','mobile, electronics, smart phone, android phone',10, 43000)
print(mobile_OnePlus)

mobile_iphone = Product(1001,'iphone 16 pro max','Good perfpmance.','mobile','mobile, electronics, smart phone, iphone',10, 153000)
print(mobile_iphone)
'''
