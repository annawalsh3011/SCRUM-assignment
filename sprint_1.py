import random
items = []
orders = []
shoppers = []

class Items():
    def __init__(self):
        self.item_name = ''
        self.item_type = ''
        self.item_price = 0
        self.expiration_date = ''
        self.item_id = ''
        self.item_quantity = 0

    def set_item_name(self, n):
          self.item_name = n
    
    def get_item_name(self):
        return self.item_name
    
    def set_item_type(self, t):
        self.item_type = t
    
    def get_item_type(self):
        return self.item_type

    def set_item_price(self, p):
        self.item_price = p

    def get_item_price(self):
        return self.item_price

    def set_expiration_date(self, d):
        self.expiration_date = d
    
    def get_expiration_date(self):
        return self.expiration_date
    
    def set_item_id(self, id):
        self.item_id = id
    
    def get_item_id(self):
        return self.item_id

    def set_item_quantity(self, q):
        self.item_quantity = q

    def get_item_quantity(self):
        return self.item_quantity
    
    def display(self):
        print(f'Item Name: {self.item_name}')
        print(f'Item Type: {self.item_type}')
        print(f'Item Price: {self.item_price}')
        print(f'Expiration Date: {self.expiration_date}')
        print(f'Item ID: {self.item_id}')
        print(f'Item Quantity: {self.item_quantity}')

def id_generator():
    number = random.randint(1000, 5000)
    cap_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_1 = random.choice(cap_letters)
    letter_2 = random.choice(low_letters)

    id = letter_1 + str(number) + letter_2

    return(id)

def items(item_name, item_type, item_price, expiration_date, item_id, item_quantity):
    global items
    c = Items()
    c.set_item_name(item_name)
    c.set_item_type(item_type)
    c.set_item_price(item_price)
    c.set_expiration_date(expiration_date)
    c.set_item_id(item_id)
    c.set_item_quantity(item_quantity)
    
    items.append(c)
    return items

class Orders():
    def __init__(self):
        self.order_quantity = 0
        self.order_id = ''
        self.shopper = ''
        self.items = '' 

    def set_order_quantity(self ,q):
        self.order_quantity = q

    def get_order_quantity(self):
        return self.order_quantity

    def set_order_id(self ,i):
        self.order_id = i

    def get_order_id(self):
        return self.order_id

    def set_shopper(self ,s):
        self.shopper = s

    def get_shopper(self):
        return self.shopper 

    def set_items(self, it):
        self.items = it
    
    def get_items(self):
        return self.items

    def display(self):
        print(f'Order Quantiy: {self.order_quantity}')
        print(f'Order ID: {self.order_id}')
        print(f'Shopper: {self.shopper}')
        print(f'Items: {self.items}')
        
def orders(order_quantity, order_id, shopper, items):
    global orders
    c = Orders()
    c.set_order_quantity(order_quantity)
    c.set_order_id(order_id)
    c.set_shopper(shopper)
    c.set_items(items)

    orders.append(c)
    return orders
    
class Shoppers():
    def __init__(self):
        self.shopper_name = ''
        self.shopper_id = ''
        self.shopper_age = ''
        self.shopper_address = ''
        self.shopper_basket = ''

    def set_shopper_name(self, n):
        self.shopper_name = n
    
    def get_shopper_name(self):
        return self.shopper_name
    
    def set_shopper_id(self, i):
        self.shopper_name = i
    
    def get_shopper_id(self):
        return self.shopper_id

    def set_shopper_age(self, a):
        self.shopper_name = a
    
    def get_shopper_age(self):
        return self.shopper_age
    
    def set_shopper_address(self, ad):
        self.shopper_address = ad
    
    def get_shopper_address(self):
        return self.shopper_address
    
    def set_shopper_basket(self, b):
        self.shopper_name = b
    
    def get_shopper_basket(self):
        return self.shopper_basket

    def display(self):
        print(f'Shopper Name: {self.shopper_name}')
        print(f'Shopper ID: {self.shopper_id}')
        print(f'Shopper Age: {self.shopper_age}')
        print(f'Shopper Address: {self.shopper_address}')
        print(f'Shopper Basket: {self.shopper_basket}')

def shoppers(shopper_name, shopper_id, shopper_age, shopper_address, shopper_basket):
    global shoppers
    c = Shoppers()
    c.set_shopper_name(shopper_name)
    c.set_shopper_id(shopper_id)
    c.set_shopper_age(shopper_age)
    c.set_shopper_address(shopper_address)

    shoppers.append(c)
    return shoppers

basket_list = []
def add_to_basket(items, quantity, stock):
    if quantity < stock:
        basket_list.append(items, quantity)
    else:
        print('Not enough stock to complete this order')