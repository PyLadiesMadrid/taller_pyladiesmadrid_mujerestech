print("Hello!")

ans = 'n'

while ans != 'y':

    ans = input('Do you want to learn python programming?  (y/n) \n')

    if ans.lower().strip() == 'y':
        print("Great answer! You can do it! Let's go!")
        break
    else:
        print('Why not? Think about it again. Please!')

