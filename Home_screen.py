from Item1 import Item
import datetime

choice = 0

print('Welcome')
print('Below is a menu')

while choice != '4':
    print('1: Add Items')
    print('2: View all items')
    print('3. Delete expired items')
    print('4: Exit')

    choice = input('Choose the number of the function you wish to use: ')

    if choice == '1':
        #add items
        name = input('Enter item name: ')
        type = input('Enter the number of the item type from: 1 = luxury, 2 = essential or 3 = gift ')
        amount = input('Enter the amount of stock you want to add')
       # expiration_date = input('Enter expiration date of product in format of dd/mm/yyyy (10/12/2018): ')
       
        print('does this item have an expiration date?')
        e_d= input('Enter 1 for yes or 2 for no')
        if e_d == '1':
            day= int(input('enter the date of expiry .i.e enter 3 if it is the 3rd  '))
            month= int(input('enter the month of expiry in numbers i.e enter 6 if it is june  '))
            year = int(input('enter the yeaar of expiry i.e. 2008  '))
            expiration_date= datetime.date(year, month, day)

            if name and type and amount and expiration_date != '':
                Item.add_item( name, type, expiration_date, amount) 
            else:
                print('item not added as not all fields were incomplete')
        else:
            if name and type and amount != '':
                expiration_date=''
                Item.add_item( name, type, expiration_date, amount)
            else:
                print('item not added as not all fields were incomplete')

        
    if choice == '2':
        all = Item.view_all_items()

        delete_choice =''
        print('Do you want to delete an item from the list?')
        delete_choice= input('Enter 1 for Yes, enter 2 to return to home screen ')
        if delete_choice== '1':
            del_item= input('enter the name of item you want to be deleted')
            Item.delete(del_item)
        else:
            print('exit')
            ##### return back to home screen
    
    if choice == '3':
        Item.delete_expired_items()