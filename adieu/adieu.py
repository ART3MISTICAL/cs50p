import inflect

p = inflect.engine()

names = [

]

while True:
    try:
        get_name = input("Name: ")
        names.append(get_name)
    except EOFError:
        print()
        break

result = p.join(names)
print('Adieu, adieu, to', result)