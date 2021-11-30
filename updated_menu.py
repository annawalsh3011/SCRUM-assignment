import customers

choice = 0

print('welcome')

while choice != '5':
    print('1: Customers')
    print('2: Suppliers')
    print('3: Stock')
    print('4: Oders')
    print('5: Exit')

    choice = input('Choose the number of the function you wish to use: ')

    if choice == '1':
       choice_1 = 0
       while choice_1 != '1':
            print('1: Home')
            print('2: Add Customer')
            print('3: Update Customer')
            print('4: View Customers')
            print('5: Customer Report')
            print('6: Delete Customer')
 
            choice_1 = input('Choose the number of the function you wish to use: ')

            if choice_1 == '1':
                choice_1 = '1'
            if choice_1 == '2':
                customer_no = input('Enter customer number: ')
                name = input('Enter customer name: ')
                address = input('Enter customer address: ')
                telephone = input('Enter customer telephone: ')
                gender = input('Enter customer gender: ')
                industry = input('Enter customer industry: ')

                customers.add_customer(customer_no, name, address, telephone, gender, industry)
            if choice == '4':
                res = customers.view_all_customer()
                print(res)

    if choice == '2':
        print('A')
    if choice == '3':
        print('A')
    if choice == '4':
        print('A')
