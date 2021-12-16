#ADD THE BASKET TOTAL
# if we're using a array for the basktet (eg list, dict)
basket_list = {'nike tech': 200, 'jordan 11s': 250, 'laptop': 500}
#def getBasketsum(basket):
    #sum = 0
    #for items in basket:
        #curent = basket[items]
        #sum = sum + curent
    #return sum


#x = getBasketsum(basket_list)
#print(x) 


# if we're using a class to represent the basket 
# only difference would be the getPrice function


#
def getBasketsum(basket):
    sum = 0
    for items in basket:
        curent = items.getPrice()
        sum = sum + curent
    return sum


class Item():
    def __init__(self):
        self.id = ''
        self.price = 0
        self.name = ''
        self.type = ''
        self.expiration_date = ''
        self.quantity = 0

def add_item( name, type, expiration_date, price ):
    self.price(price, self)
        global stock_items


for a in range(len(stock_items)):
            if stock_items[a].get_name() == name:
                q= stock_items[a].get_quantity()
                q=  str(q)
                print(q)
                #stock_items[a].set_quantity(q)


for a in stock_items:
    if a.get_name() == name:
        q = a.get_quantity()
        a.set_quantity() += 1


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