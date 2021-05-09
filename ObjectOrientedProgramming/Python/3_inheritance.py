"""
Inheritance allows us to inherit attributes and methods from parent classes --> Useful because we can reuse attributes/methods in subclasses
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
                                                                    
    def fullname(self):                                      
        return self.first + ' ' + self.last

    def apply_raise(self):                                       
        self.pay = int(self.pay * self.raise_amount)             


class Developer(Employee):                                          # inheriting all properties from Employee class into Developer class                                      
    #pass
    raise_amount = 1.10                                             # single class variables or attributes can be modified in subclasses
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)                          # inherit attributes first, last and pay from the parent class. No need to rewrite the code. 
        #Employee.__init__(self, first, last, pay)                  # this is equivalent to the line above (super.__init__())
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            


#emp_1 = Employee('Bob', 'Alice', 100)
#emp_2 = Employee('Test', 'User', 200)
# print(emp_1.email)
# print(emp_2.email)

dev_1 = Developer('Bob', 'Alice', 100,'Python')
dev_2 = Developer('Test', 'User', 200,'Java')
print(dev_1.__dict__)
print(dev_2.__dict__)

# print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Tom','Jerry',1000,[dev_1, dev_2])
mgr_1.print_emps()
mgr_1.remove_employee(dev_1)
mgr_1.print_emps()
mgr_1.add_employee(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1,Manager))
print(issubclass(Manager,Employee))