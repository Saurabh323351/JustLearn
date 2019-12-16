
"""
In Aggregation ,the relationship between classes which have some association is represented by a keyword
 Has-A

  Employee Has-A Salary

key differences : 1) here association is denoted by Has-A keyword
                2) here Salary and Employee are independent of each other
                3)here Salary and Employee are unidirectional
"""

class Salary:

    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:

    def __init__(self,name,age,salary_instance):
        self.name=name
        self.age=age
        self.obj_salary=salary_instance

    def total_salary(self):

        return self.obj_salary.annual_salary()

salary_instance=Salary(90000,30000)
emp=Employee('saurabh',23,salary_instance)
print(emp.total_salary())

