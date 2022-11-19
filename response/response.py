import validators
print('valid') if validators.email(input('Enter email address: ')) == True else print('invalid')