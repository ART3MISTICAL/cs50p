grocery_list = {

}

while True:

    try:
        get_item = input()
        grocery_list

    except EOFError :
        break

    if get_item.upper() in grocery_list:
        grocery_list[get_item.upper()] += 1
    else:
        grocery_list[get_item.upper()] = 1

for get_item in sorted(grocery_list.keys()):
    print(grocery_list[get_item], get_item)
