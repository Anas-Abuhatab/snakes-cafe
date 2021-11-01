menu = {
    'Wings':0,
    'Cookies':0,
    'Spring Rolls':0,
    'Salmon':0,
    'Steak':0,
    'Meat Tornado':0,
    'A Literal Garden':0,
    'Ice Cream':0,
    'Cake':0,
    'Pie':0,
    'Coffee':0,
    'Tea':0,
    'Unicorn Tears':0
}

welCome = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""

order =[]

print(welCome)

while True:
    userInput = input('> ')
    if userInput == 'quit':
        break
    elif userInput in menu:
        menu[userInput] +=1
    else :
        print("**Please choose item **")
    for key ,value in menu.items():
        if value >=1 :
            print( f"** {value} order of {key} have been added to your meal **")
            order.append(f"{value} order of {key}")
        else:
            continue
