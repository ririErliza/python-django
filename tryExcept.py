'''----------------TRY EXCEPT------------------------'''

# teling the user that the input is invalid

# try:
#     x=int(input('Input an integer : '))
#     print(x)
# except:
#     print('Something went wrong, that\'s not integer')
#Input an integer : r
#Something went wrong, that's not integer

try:
    x=int(input('Input an integer : '))
    print(x)
except ValueError:
    print('Value is not integer')

# Input an integer : e
# Value is not integer