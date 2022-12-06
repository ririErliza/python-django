#---------------------------------------------------printing----------------------------------------------------------------------

print('Hello World, welcome')
print('Welcome')
print('My Name is Lili I am', 100, 'years')


#---------------------------------------------------variables-----------------------------------------------------------------------

name = 'Tim'

"""
name is the name of variable

'Tim' is the value
"""

print(name)

print(name + 'is a boy')
print(name + 'is 18')
print(name + 'is from Turkey')

#-----------------------------------------------------data types : string--------------------------------------------------------------------



name = 'Roy'
age = 18

print(name)
print(name + 'is a boy')
print(name,'is', age)


"""
string
number/integer
boolean
"""

##### String #####

print('Hi. How are you')
print('Hi. \nHow are you')
print('Hi. \'How are you\'') #using backslash to show a quote

fruit = 'Banana'
print(fruit[2]) #print letter at index 2
print(fruit.upper())
print(fruit.islower()) #false coz must all lowercase
print(fruit.lower())
print(fruit.isupper()) #false coz must all uppercase
print(fruit.upper().isupper()) #true
print(fruit) #Banana
print(len(name)) #3 to get the length of a string
print(fruit.index('a')) # 1
print(fruit.replace('a', 'i')) #Binini


#-----------------------------------------------------data types : number/integer --------------------------------------------------------------------

print(75) # print number directly

number = 79
print(number) # print variable with value of integer/number

print(1+2)  # perform arithmatic operation
print(2.5 + 1.25)
print( 64/8)
print(5*3)
print(20%6)

number2 = str(number) #convert number to string
print(number2)
# print('number is' + number) #concatenate string with number will give error result
print('this is the number ' + number2) #work out because number2 is already converted to string

print(-5)
print(abs(-5)) #will give absolute number of this value, 5
print(max(4,1,6)) #get highest number, 6
print(min(2,1,-3)) # -3
print(round(3.5)) #4
print(bin(3)) # return the binary string, 0b11

# methods above are built in
# there are methods that need importing  math library first


###### number method that we need to import first ########
from math import * # importing everything with this asterix

print(sqrt(100)) #10.0

#-----------------------------------------------------getting user's input--------------------------------------------------------------------
animal = input('Input Your Fav Animal: ') # saving the input that user type in a variable called animal
flower = input('Input Your Fav Flower: ')
print('Your fav animal is ' + animal + ' and your fav flower is ' + flower)