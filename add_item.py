# finding an item 
product_list = {'watch':100, "phone":800, "tracksuit": 200, "ps5":500, "car":10000}
def searchProduct(search): 
    search = input('input a keyword to search for an item> ')
    decision = 'not found'
    #while product == 'not found':       
    for item in product_list:
        if item == search:
            decision = 'found'
            #return(decision)
    return(decision)
# if x = found:
    #add to basket
x = searchProduct(product_list)
print(x)

