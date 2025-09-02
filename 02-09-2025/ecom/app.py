#  Driver code

from product_manager import create_product, read_all, read_by_id
from product_manager import update, delete_by_id
from product import Product

def menu():
    message = '''
The menu choices are 
1  - Create Product
2  - Read All Products
3  - Read By Id
4  - Update
5  - Delete
6  - Exit / logout
Your choice:'''
    choice = int(input(message))
    if choice == 1:
        name = input('Name :')
        description = input('Description :')
        category = input('Category :')
        tags = input('Tags :')
        stock = int(input('Stock :'))
        price = int(input('Price :'))
        id = -1

        product = Product(id, name, description, category, tags, stock, price)
        create_product(product)
        print('Product created successfully.')

    elif choice == 2:
        products = read_all()
        print('Products Catalog :')
        for product in  products:
            print(product)

    elif choice == 3:
        id = int(input('ID:'))
        product = read_by_id(id)
        if product == None:
            print('Product not found ')
        else:
            print(product)
        
    elif choice == 4:
        id = int(input('ID:'))
        old_product = read_by_id(id)
        if old_product is None:
            print('product not found. ')
        else:
            print(old_product)
            name = input('Name :')
            description = input('Description :')
            category = input('Category :')
            tags = input('Tags :')
            stock = int(input('Stock :'))
            price = int(input('Price :'))

            new_product = Product(id, name, description, category, tags, stock, price)
            update(new_product)
            print('Product updated successfully. ')

    elif choice == 5:
        id = int(input('ID:'))
        old_product = read_by_id(id)
        if old_product is None:
            print('product not found. ')
        else:
            print(old_product)
            if input('Are you sure to delete (y/n)?') == 'y':
                delete_by_id(id)
                print('Product deleted successfully. ')
    return choice

def menus():
    print('product Management App')
    choice = menu()
    while choice != 6:
        choice = menu()
    print(' Thank you for using App')

menus()