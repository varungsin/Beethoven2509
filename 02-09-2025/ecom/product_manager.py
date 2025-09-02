#  Task code

products = []
#  CURD - Create, Read All, Read By Id, Update, delete
#                       Read By product

def create_product(product):
    global products
    if len(products) == 0:
        product.id = 1
    else:
        product.id = products[len(products) -1].id +1
    products.append(product)

def read_all():
    return products

def read_by_id(id):  #returning first index of the product
    for product in products:
        if product.id == id:
            return product
    return None

def update(product):
    old_product = read_by_id(product.id)
    if old_product == None:
        return
    old_product.name = product.name
    old_product.description = product.description
    old_product.category = product.category
    old_product.tags = product.tags
    old_product.stock = product.stock
    old_product.price = product.price 

def delete_by_id(id):
    global products
    product = read_by_id(id) # id of product
    products.remove(product) # delete by id 