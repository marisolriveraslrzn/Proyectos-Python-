
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'El empleado {self.name} tiene {self.age} años y {self.salary}de salario.'

    def __repr__(self):
        return F'Empleado(name={self.name}, age={self.age}, salary={self.salary}'