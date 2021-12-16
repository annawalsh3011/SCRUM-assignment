import random
import string
import datetime

stock_items=[]
expired_items=[]
basket_list=[]

class Item():
    def __init__(self):
        self.id = ''
        self.name = ''
        self.type = ''
        self.expiration_date = ''
        self.quantity = 0
        self.price= 0

    def set_id(self, i):
        self.id  = i

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
    
    def set_price(self, p):
        self.price  = p

    def get_price(self):
        return self.get_price

    def __str__(self):
        return 'Id: '+ str(self.id) + ' Name: ' + str(self.name) + ' Type: ' +str(self.type)  + ' Expiration Date: ' +str(self.expiration_date) + ' Price: ' +str(self.price) + ' Quantity: ' +str(self.quantity) 


    def add_item( name, type, expiration_date, amount):
        global stock_items

        for a in stock_items:
            if a.get_name() == name:
                val = int(a.quantity) + int(amount)
                a.set_quantity(val)
                return stock_items


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
            i.set_type('Gift')
        
        i.set_expiration_date(expiration_date)
        
        if type == '1':
            i.set_price(50)
        if type == '2':
            i.set_price(30)
        if type == '3':
            i.set_price(20)

        i.set_quantity(amount)
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


    def delete_expired_items():
        for i in range(len(stock_items)):
            a=stock_items[i-1].get_expiration_date()
            if a != '' and a < datetime.date.today():
                stock_items.remove(stock_items[i-1])
                expired_items.append(stock_items[i-1])


def add_basket(name, q):
    for i in range(len(stock_items)):
        if stock_items[i-1].get_name() == name:
            a  = stock_items[i-1]
            a.set_quantity(q)
            basket_list.append(a)
    
    for b in basket_list:
        print(b)

def sum_basket(name, q):
    L = 'Luxury'
    G= 'Gift'
    E= 'Essential'
    count = 0
    q = int(q)
    for i in range(len(stock_items)):
        if stock_items[i-1].get_name() == name:
            for b in range(len(basket_list)): 
                if basket_list[b-1].get_type() == L:
                    vat = q * 50 * .2
                    vat = int(vat)
                    count = int(count)
                    count = count + (50 * q) + vat
                if basket_list[b-1].get_type() == G:
                    vat = q * 20 * .05
                    vat = int(vat)
                    count = int(count)
                    count = count + (20 * q) + vat
                if basket_list[b-1].get_type() == E:
                    vat = q * 30 * .1
                    vat = int(vat)
                    count = int(count)
                    count = count + (30 * q) + vat

                
            return count  



def change_calculator(total_cost, amount_paid):
    total_change= amount_paid- total_cost
    total_change = round(total_change, 2)
    print(f"Total_change: {total_change}")

    hundred_euros = int(total_change / 100)   # the number of hundred euros
    new_balance=total_change-(hundred_euros*100) # getting the remainder
    fifty_euros = int(new_balance/50)
    new_balance=new_balance-(fifty_euros*50)
    twenty_euros = int(new_balance/20)
    new_balance=new_balance-(twenty_euros*20)
    ten_euros = int(new_balance/10)
    new_balance=new_balance-(ten_euros*10)
    five_euros = int(new_balance/5)
    new_balance=new_balance-(five_euros*5)
    two_euros = int(new_balance/2)
    new_balance=new_balance-(two_euros*2)
    one_euros = int(new_balance/1)
    new_balance=new_balance-(one_euros*1)
    fifty_cent= int(new_balance/(0.5))
    new_balance= new_balance-(fifty_cent*(0.5))
    twenty_cent= int(new_balance/(0.2))
    new_balance= new_balance-(twenty_cent*(0.2))
    ten_cent= int(new_balance/(0.1))
    new_balance=new_balance-(ten_cent*(0.1))
    five_cent= int(new_balance/(0.05))
    new_balance=new_balance-(five_cent*(0.05))
    two_cent= int(new_balance/(0.02))
    new_balance=new_balance-(two_cent*(0.02))
    one_cent=int(new_balance/(0.01)) 

    Change=(f'{hundred_euros}-  €100 note, {fifty_euros}- €50 note, {twenty_euros}- €20 note, {ten_euros}- €10 note , {five_euros}- €5 note, {two_euros}- €2 coin, {one_euros}- €1 coin, {fifty_cent}- 50 cent coin, {twenty_cent}- 20 cent coin,  {ten_cent} - 10 cent coin,  {five_cent} - 5 cent coin,  {two_cent} - 2 cent coin,  {one_cent} - 1 cent coin')
    print(Change)

    print("do you want to clear everything?")
    print("1. Yes")
    print("2. No")
    option= input("enter either 1 or 2")
    if option=='1':
        total_cost=0
        total_change=0
    else:
        print('it is not cleared')
    return Change
    

