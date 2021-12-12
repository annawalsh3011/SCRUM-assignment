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

# first example
# when the user enters each number manually, it wokrs 
total_cost= float(input('enter the total amount of the basket: '))
amount_paid = float(input("Please enter an amount you are paying with: "))
change_calculator(total_cost, amount_paid)

#second example taking it from the previous parts
amount_paid = float(input("Please enter an amount you are paying with: "))


total__basket_cost= 
change_calculator(total_basket_cost, amount_paid)