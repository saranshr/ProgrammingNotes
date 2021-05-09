""" 
Why should classes be used?
--> Classes allow data and functions to be grouped in order to be easily reused
    --> Data is known as Attributes of a class
    --> Functions are known as Methods of a class
 """

"""
class Employee:
    pass                   # in order to create an empty class

#A class is a kind of a blueprint of that 'idea', in this case the Employees of a company.
#An instance of a class is the actual object being created from that class, e.g. Employee1, Employee2, etc. Each employee will have
#the same properties as were defined in the 'blueprint' class (attributes, methods)

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)                # each instance is independent of the other and is stored at different locations in memory
print(emp_2)                # instance variables contain data, which is unique for each employee


emp_1.first = 'Bob'
emp_1.last = 'Alice'
emp_1.email = 'Bob.Alice@example.com'
emp_1.pay = 100

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@example.com'
emp_2.pay = 200
 
print(emp_1.email)
print(emp_2.email)


#No advantage of using classes here, since the instances are being defined each time. Therefore, we create an init method within the class
#where we make the definitions

"""

class Employee:
    
    def __init__(self, first, last, pay):             # the 'self' argument is necessary, since the instances which will call the attributes or
        self.first = first                            # methods of this class are themselves arguments of the class --> they are referenced by 'self'
        self.last = last                              
        self.pay = pay
        self.email = first + '.' + last + '@example.com'
    
    def fullname(self):
        return self.first + ' ' + self.last

emp_1 = Employee('Bob', 'Alice', 100)
emp_2 = Employee('Test', 'User', 200)

print(emp_1.fullname())
print(Employee.fullname(emp_1))                       
# these two statements are equivalent. In the first statement, the instance emp_1 is being used to call the method Fullname of the class Employee
# in the second statement, the method is being directly called via the class. Hence the instance needs to be provided as an argument. In the first
# statement, the instance itself is the argument (referenced in the class by self), therefore no further arguments needs to be passed