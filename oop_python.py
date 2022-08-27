'''

Classes  - Class objects

Eg:
class Person:

    def set_details(self):
        self.name='' =>instance variables/attributes
        self.age=''  
    => behaviours/methods
    def display(self):
        print("")
    def greet(self):         => self indicates the object that is calling. it is compulsory, it should be present
        print("")

#classes are also objects in python.

Objects - instance objects

create instance objects:p1= Person()

call methods of objects=> 

p1.display()
p2.greet()

p1.name

'''


#Exercise 1:

class bankAccount:
    def set_details(self, name, balance=0):
        self.name=name
        self.balance=balance
        
    def display(self):
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        
    def withdraw(self,amount):
        self.balance-=amount
    
    def deposit(self,amount):
        self.balance+=amount
    
    
b1=bankAccount()
b2=bankAccount()

b1.set_details('A')
b2.set_details('B')

b1.display()
b2.display()

b1.deposit(100)
b2.deposit(500)

b1.display()
b2.display()

b1.withdraw(50)
b2.withdraw(100)

b1.display()
b2.display()
        

'''
# __init__(self,name,balance) method- method is executed once the instance object is created-> no need to call set_details, 
# automtically executes the content on init method 

=>called dunder init-> dunder is shortform of double underscore

the parameters for init method will be sent through object initiation=> p1=Person('A',100)


* other methods like dunder methods=> magic methods

*only one __init__ in a class
'''

'''
# Data Hiding

Private and Public data & methods:

private- used only by the methods inside the class=> implementation
public- accessed from outside the class as well => interface =>clients can access this

*But in python everything inside a class is public
--> naming convention for data and methods to be accessed only inside the class. put underscore at the start of name. _data1, _data2, _methodA()
can be accessed outside, but should not be accessed
if really want to make private=> use __

*use trailing underscores to avoid name clashed

''' 
        

