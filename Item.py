import random
import string
stock_items=[]

class Item():
    def __init__(self):
        self.id = ''
        self.name = ''
        self.type = ''
        self.expiration_date = ''
        self.quantity = 0

    def set_id(self, i):
        self.id  = id

    def get_id(self):
        return self.id

    def set_name(self, n):
        self.name  = n

    def get_name(self):
        return self.name    

    def set_type(self, t):
        self.type  = t

    def get_type(self):
        return self.type

    def set_expiration_date(self, e):
        self.expiration_date  = e

    def get_expiration_date(self):
        return self.expiration_date
    
    def set_quantity(self, q):
        self.quantity  = q

    def get_quantity(self):
        return self.get_quantity
    
    def __str__(self):
        return 'Id: '+ str(self.id) + ' Name: ' + str(self.name) + ' Type: ' +str(self.type)  + ' Expiration Date: ' +str(self.expiration_date)  + ' Quantity: ' +str(self.quantity) 


    def add_item( name, type, expiration_date ):
        global stock_items

        for a in range(len(stock_items)):
            if stock_items[a].get_name() == name:
                q= stock_items[a].get_quantity()
                q=  str(q)
                print(q)
                #stock_items[a].set_quantity(q)
                
    ##################################################### adding to an item that has already been there

    ##########showing the id in the list
        # Create a Customer object
        i = Item()

        #creating random id
        alphabet= list(string.ascii_lowercase)
        b=random.randint(0,25)
        letter=alphabet[b]
        k=random.randint(0,25)
        letter1=alphabet[k]
        n=random.randint(0,10000)
        id= str(n) + letter + letter1
        id = str(id)

        i.set_id(id)
        i.set_name(name)

        if type == '1':
            i.set_type('Luxury')
        if type == '2':
            i.set_type('Essential')
        if type == '3':
            i.set_type('Luxury')
        
        i.set_expiration_date(expiration_date)
        i.set_quantity('1')
        # Add it to the stock list
        stock_items.append(i)

        return stock_items

    def view_all_items():
        for i in range(len(stock_items)):
            print(stock_items[i].__str__())
    
    def delete(name):
        for i in range(len(stock_items)):
            if stock_items[i-1].get_name() == name:
                stock_items.remove(stock_items[i-1])

        