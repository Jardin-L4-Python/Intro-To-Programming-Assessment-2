#Vending Machine

#Display a message greeting the user.
#Print using strings.
print("Hello! Welcome to the Vending Machine!\n")

#Display a message telling the user to select an item they want.
print("Feel free to select an item you'd like to buy!\n")

#Display the name, code, and price of the items.
#Make the items list and dictionaries.
items = [
    {
        'code':0,
        'name':'Snickers',
        'price':4
    },
    {
        'code':1,
        'name':'Gummy bears',
        'price':7
    },
    {
        'code':2,
        'name':'Twix',
        'price':4
    },
    {
        'code':3,
        'name':'Oreo',
        'price':4
    },
    {
        'code':4,
        'name':'Doritos chips',
        'price':5
    },
    {
        'code':5,
        'name':'Cheetos chips',
        'price':5
    },
    {
        'code':6,
        'name':'Apple juice',
        'price':3
    },
    {
        'code':7,
        'name':'Orange juice',
        'price':3
    },
    {
        'code':8,
        'name':'Chocolate milk',
        'price':4
    },
    {
        'code':9,
        'name':'Strawberry milk',
        'price':4
    },
    {
        'code':10,
        'name':'Coca cola',
        'price':3
    },
    {
        'code':11,
        'name':'Fanta',
        'price':3
    },
{
        'code':12,
        'name':'Sprite',
        'price':3
    },
    {
        'code':13,
        'name':'Water',
        'price':2
    },
    {
        'code':14,
        'name':'Iced tea',
        'price':3
    },
    {
        'code':15,
        'name':'Gatorade',
        'price':4
    }
]
is_quit = False
item = ''
#Add the code value linearly.
while is_quit == False:
#While loop
#For loop
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")
#Display a message asking the user to enter the code number of the item they want to buy.
    query = int(input("Enter the code of the item you want to buy: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('CODE UNAVAILABLE')
#Put the price and details of the user's selected item.
#Then it will ask the user to enter the price amount.
#If it matches the price of the user's selected item, they get it.
#If not, then the user won't get their selected item.
    else:
        print(f"Nice! {item['name']} will cost you {item['price']} dollars")

        price = int(input(f"Enter {item['price']} dollars to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        else:
            print(f"Please enter only {item['price']} dollars")
#Lastly, ask the user if they want to continue or quit the machine.
    print("Enjoy and have a great day!")
    query = input("To quit the machine simply enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')







