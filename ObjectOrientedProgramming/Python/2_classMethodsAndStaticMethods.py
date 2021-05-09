""" 
Distinguishing between:
    regular methods     --> the instances are automatically provided as an argument (self)
    class methods       --> the class is automatically provided as an argument (cls)
    static methods      --> no argument is provided automatically
"""
class Employee:

    raise_amount = 1.04                                             
                                                                    
    num_of_employees = 0                                            
                                                                    
    def __init__(self, first, last, pay):             
        self.first = first                                          
        self.last = last                                            
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

        Employee.num_of_employees += 1                             
                                                                    
    # a regular method in a class takes the instance, referenced with 'self', as the first argument                                                                    
    def fullname(self):                                      
        return self.first + ' ' + self.last

    def apply_raise(self):                                       
        self.pay = int(self.pay * self.raise_amount)             
    
    # creating a class method, i.e. a method which takes a class as an argument
    @classmethod                                            # a so called decorator is used
    def set_raise_amt(cls, amount):                         # 'cls' refers to the class, just as 'self' refers to each instance above
        cls.raise_amount = amount               
    
    # Assume the use case, that data is provided in a string as follows: 'firstname-lastname-pay', e.g. 'Tom-Jerry-500'. 
    # Of course, we can parse the string for each hyphen and store the data in separate variabels and create class instances from those variables
    # but that is a lot of work. Instead, we realise this via a further class method, as follows:
    
    @classmethod
    def from_string(cls,emp_str):                           # from_string is just the name, from_... is the convention for such use cases
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)                               # create the instance of the class after parsing the input string at each hyphen
    # This is an example of using a classmethod as a so-called alternative constructor        

    # We move on to Static Methods
    # E.g. we want a function which takes the date and determines whether thats a work day 
    # Whilst this does have a connection to our class Employee, it doesn't depend on any instance or attribute of the Employee class
    
    @staticmethod
    def is_workday(day):                                    # no 'automatic' arguments are passed, so we can directly pass the arguments we need for the function
        if day.weekday() == 5 or day.weekday() == 6:     # In Python, the weekday() method returns the following: 0=Mon, 1=Tue, 2=Wed, 3=Thur, 4=Fri, 5=Sat, 6=Sun
            return False
        return True
    # The obvious reason why we can use a staticmethod for this problem is, because the function does not use any dependencies (class, instances) within the method
    # On the other hand, in the functions above, e.g. from_string or set_raise_amt, we clearly use the class itself (cls). Therefore these functions cannot be declared as staticmethods


emp_1 = Employee('Bob', 'Alice', 100)
emp_2 = Employee('Test', 'User', 200)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# we use the class method to increment the raise amount to 5%
Employee.set_raise_amt(1.05)                                # it is sufficient to pass the argument 'amount'. The argument 'cls' is passed automatically
# this is the equivalent of running Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_3 = Employee.from_string('Tom-Jerry-500')           # create new employee (instance) using the class method
print(emp_3.__dict__)                                   # namespace of new employee created

import datetime
my_date = datetime.date(2016,7,11)
print('my_date: ', my_date)
print('weekday ', my_date.weekday()) 
print(Employee.is_workday(my_date))