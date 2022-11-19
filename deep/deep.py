ans = input('What is the answer to the great question of life, the universe and everything?\n')

# print(ans.lower().strip())

if ans.lower().strip() == '42' or ans.lower().strip() == 'forty two' or ans.lower().strip() == 'forty-two':
    print ('Yes')
else:
    print('No')
