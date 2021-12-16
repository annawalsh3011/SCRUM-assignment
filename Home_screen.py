from Item1 import Item
from Item1 import add_basket
from Item1 import sum_basket
from Item1 import change_calculator
import datetime




print('Welcome')
print('Below is a menu')
a_choice=0 
while a_choice != '3':
    a_choice = input('Enter 1 if you are a  staff member or 2 if you are a customer:  ')

    if a_choice == '1':
        choice = 0
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

            if choice == '4':
                a_choice = '0'

    if a_choice == '2':
        choice_2 = 0
        while choice_2 != '4':
            print('1: view all items')
            print('2: Purchase items')
            print('3. Calculate change')
            print('4: Exit')

            choice_2 = input('Choose the number of the function you wish to use: ')
            

            if choice_2 =='1':
                all = Item.view_all_items()

            if choice_2 == '2':
                option = int(input('Enter the number of item you want to purchase: '))
                for i in range(option):
                    name= input('enter the exact name of the product from the list above that you wish to purchase')
                    quantity = int(input('enter the amount of items you wish to purchase'))
                    add_basket(name, quantity)

                    res = sum_basket(name, quantity)
                print(res)
            
            if choice_2 == '3':
                amount_due = res
                amount_due = float(amount_due)
                print(f'The amount dew is {amount_due}')
                amount_pay = float(input('Enter the amount you want to pay: '))
                change = change_calculator(amount_due, amount_pay)


