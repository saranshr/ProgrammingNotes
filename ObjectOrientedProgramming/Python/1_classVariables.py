class Employee:

    raise_amount = 1.04                                             # Class Variable, accessbile from the class as well as all instances of 
                                                                    # the class.
    num_of_employees = 0                                            # we want to increment this class variable by 1 everytime an instance of the class is created.
                                                                    # This can be done in the __init__ method, since it is called everytime an instance of the class is created.                                                                
    def __init__(self, first, last, pay):             
        self.first = first                                          # these are Instance Variables
        self.last = last                                            # i.e. Variabels which are created for each instance of the class created
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

        Employee.num_of_employees += 1                              # Here we use Employee.num_of_employees instead of self.num_of_employees 
                                                                    # because for this class variable, there is no use case where the variable would
                                                                    # be modified for a single instance
    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):                                       
        self.pay = int(self.pay * self.raise_amount)                # we use self.raise_amount instead of Employee.raise_amount, since there are
                                                                    # use cases where the class variable raise_amount may be needed to be modified for
                                                                    # single instances                
                                                                    
                                                                    
print(Employee.num_of_employees)                                    # returns 0, since no instance of the class has been created yet

emp_1 = Employee('Bob', 'Alice', 100)
emp_2 = Employee('Test', 'User', 200)

# print(emp_1.raise_amount)                                           # class variable being called from an instance of the class
# print(Employee.raise_amount)                                        # class variable being called directly from the class
# print(emp_2.raise_amount)

# # Accessing the namespace of a class instance
# print(emp_1.__dict__)
# # Accessing the namespace of the class
# print(Employee.__dict__)

Employee.raise_amount = 1.05                                        # modify the class variable
#emp_1.first = Blah                                                 # an instance variable cannot be modified --> it was given as an argument when 
                                                                    # the instance was created
print(Employee.raise_amount)
# However, the class variable can be modified just for a particular instance, and remains unchanged for the remaining instances. For example:

print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06

print(emp_1.raise_amount)                                           # the class variable has been modified for the instance emp_1
print(emp_2.raise_amount)                                           # but it remains unchanged for the other instance and for the class as a whole
print(Employee.raise_amount)

# We have not actually 'modified' the class variable raise_amount. Instead, we have created an instace variable within the instance emp_1 called
# raise_amount and set it to 1.06. Therefore the class variable raise_amount remains unchanged. When we call the variable emp_1.raise_amount, first 
# the instance is searched for a variable of that name, if that doesn't exist then the class is searched for a variable of that name. Hence, by running
# emp2.raise_amount, we would not find an instance variable of that name, so it uses the class variable (set at 1.05) instead
# --> This shows, that instance variables can be created arbitrarily for that specific instance. An example is shown below, with the 'modified' 
# namespaces of each instance

emp_2.hobbies = 'Tennis'                                            # creating a new instance variable (hobbies) for the instance emp_2 
print(emp_1.__dict__)                                               # the namespace of the instance emp_1 has grown by the element 'raise_amount'
print(emp_2.__dict__)                                               # the namespace of the instance emp_2 has grown by the element 'hobbies'
print(Employee.__dict__)                                            # the namespace of the class remains unchanged

print(Employee.num_of_employees)                                    # returns 2, since two instances (emp_1 and emp_2) of the class have been created