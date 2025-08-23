from EmployeesManager import *


class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeesManager()

    def print_menu(self):
        print("\nOpciones del programa: ")
        messages = [
            '1) Agregar nuevo empleado',
            '2) Lista de empleados',
            '3) Eliminar empleados por edad',
            '4) Actualizar salario por nombre',
            '5) Fin del programa'
        ]
        print('\n'.join(messages))
        msg = f'Ingrese su elección (del 1 al {len(messages)}):  ' 
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.EmployeesManager.add_employee()
            elif choice == 2:
                self.EmployeesManager.list_employee()
            elif choice == 3:
                age_from = int(input("Ingrese la edad: \n"))
                age_to = int(input("Tiene: "))
                self.EmployeesManager.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input("Ingrese nombre del empleado: \n")
                salary = input("Ingrese salario del empleado: \n")
                self.EmployeesManager.update_salary_by_name(name, salary)
            else:
                break