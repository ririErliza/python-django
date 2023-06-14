
'''-----------------CLASS----------------------'''

class Myclass:
    x = 5

p1 = Myclass()
print(p1.x) 

# 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age

p1 = Person('John', 87)
print(p1.name) # John
print(p1.age) # 87


name = input ('Enter your name: ')
age = input('Enter your age: ')
p1 = Person(name,age)
print(p1.name)
print(p1.age)

# Hill
# 65

