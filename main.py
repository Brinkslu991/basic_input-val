# Lucas Brinks, Keily Drogt, Qwynn darnell
# Current date
# Validating String Input (Tiered Assignment)

# Are you and your partner working on Level 1, Level 2 or Level 3 today?
# Working on Level...

# Level 2

numb = input('Enter a number: ')

if len(numb) > 4 and numb.isdigit() == True:
    print('This number works.')
elif not len(numb) > 4:
    print('You failed.')
elif not numb.isdigit() == True:
    print('You failed in a different way.')