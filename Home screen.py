from Item import Item

choice = 0

print('Welcome')
print('Below is a menu')

while choice != '3':
    print('1: Add Items')
    print('2: View all items')
    print('3: Exit')

    choice = input('Choose the number of the function you wish to use: ')

    if choice == '1':
        #add items
        name = input('Enter item name: ')
        type = input('Enter the number of the item type from: 1 = luxury, 2 = essential or 3 = gift ')
        expiration_date = input('Enter expiration date of product in format of dd/mm/yyyy (10/12/2018): ')
        if name and type and expiration_date != '':
            Item.add_item( name, type, expiration_date) 
        else:
            print('item not added as not all fields were incomplete')


        ####When an item is added it gets a unique id and the number of items (quantity) of this item type are incremented. 
        
        # A return button will bring the user back to the items main home screen.

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