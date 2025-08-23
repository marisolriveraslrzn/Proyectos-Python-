from utility import *
from Employee import *


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nIntroduce los datos del empleado')
        name = input("Introduzca el nombre del empleado: ")
        age = input_is_valid("Ingrese la edad del empleado: ")
        salary = input_is_valid("Ingrese el salario del empleado: ")
        self.employees.append(Employee(name, age, salary))

    def list_employee(self):
        if len(self.employees) == 0:
            print("\n¡La lista de empleados está vacía!")
            return
        else:
            for emp in self.employees:
                print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        for emp in self.employees:
            if age_from <= emp.age <= age_to:
                print(f"\tEliminando empleado {emp.name}")
                self.employees.remove(emp)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error: No se encontró ningún empleado')
        else:
            emp.salary = salary