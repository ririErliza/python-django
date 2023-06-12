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
# animal = input('Input Your Fav Animal: ') # saving the input that user type in a variable called animal
# flower = input('Input Your Fav Flower: ')
# age= int(input('Input your age: ')) # this is integer not a string
# print('Your fav animal is ' + animal + ' and your fav flower is ' + flower + ' also you are', age, 'years old')



#-----------------------------------------------------simple word replacement-----------------------------------------------------------
# sentence = input('Enter your sentence: ')
# print('Your sentence is: ', sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1,word2))

#------------------------------------------------------------LIST---------------------------------------------------------------------

countries = ['UK', 'Ghana', 'Nigeria', 'Australia']
print(countries) # ['UK', 'Ghana', 'Nigeria', 'Australia']
print(countries[0]) # UK
print(countries[-1]) # Australia  --- will get the value from the back
print(countries[2][0]) # N   --- getting the initial letter of the country at index 2
print(countries[1:]) # ['Ghana', 'Nigeria', 'Australia']
print(countries[2:4]) # ['Nigeria', 'Australia']
print(type(countries)) # <class 'list'>

countries[0] = 'USA'  # replace UK with USA
print(countries) # ['USA', 'Ghana', 'Nigeria', 'Australia']

print(len(countries)) #4

countries [2] = 2
countries [3] = True



print(type(countries[2])) # <class 'int'>
print(type(countries[3])) # <class 'bool'>

print(countries)

laptops =list(('Dell', 'HP', 'Lenovo', 'MAC'))  #another way to create a list
print(laptops) # ['Dell', 'HP', 'Lenovo', 'MAC']

#-----------------LIST METHODS------------------
list1 =[1,2,3,4,5]
list2 = ['banana', 'apples', 'mangos','oranges']

#joining list
list1.extend(list2)
print(list1)
#answer: [1, 2, 3, 4, 5, 'banana', 'apples', 'mangos', 'oranges']

#adding data to the list
list2.append('cherries')
print(list2)
#answer:['banana', 'apples', 'mangos', 'oranges', 'cherries']

list2.insert(1,'pears')
print(list2)
#answer : ['banana', 'pears', 'apples', 'mangos', 'oranges', 'cherries']
# data inserted at specific position

#removing data from list
list2.remove('banana')
list2.remove('oranges')
list2.remove('apples')
print(list2)
#answer : ['pears', 'mangos', 'cherries']

#getting the length of the list
print(len(list2))
#answer: 5
print(len(list1))
#answer: 9

#emptying thee list
list1.clear()
print(list1) # [] (the list is now empty)
