amount_due = 50

print ('Amount due:', amount_due)

while True:
    amount_payed = int(input('Insert coin: '))
    if amount_payed == 25 or amount_payed == 5 or amount_payed == 10:
        amount_due -= amount_payed

    if amount_due <= 0:
        print ('Charged owed:', abs(amount_due))
        exit()

    else:
        print ('Amount due:', amount_due)