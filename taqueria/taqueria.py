index = {
    "Baja Taco"         :       4.00,
    "Burrito"           :       7.50,
    "Bowl"              :       8.50,
    "Nachos"            :       11.00,
    "Quesadilla"        :       8.50,
    "Super Burrito"     :       8.50,
    "Super Quesadilla"  :       9.50,
    "Taco"              :       3.00,
    "Tortilla Salad"    :       8.00
}

amount = 0.00

while True:
    try:
        get_item = input('Item: ').title()
        amount = amount + index[get_item]
        print ('Total: $','{:.2f}'.format(amount), sep = '' )
    except EOFError :
        quit()
    except:
         pass