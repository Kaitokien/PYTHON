path = input()
check = path.split('.')
if check[1].lower() == 'py':
    print("yes")
else:
    print('no')