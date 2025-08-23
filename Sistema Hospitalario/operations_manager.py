from specialization import Specialization
from utility import input_is_valid


class OperationsManager:
    def __init__(self):
        self.specs = []

    def print_menu(self):
        print("Opciones del programa: ")
        messages = [
            '1) Añadir nuevo paciente',
            '2) Imprimir todos los pacientes',
            '3) Obtener siguiente paciente',
            '4) Wliminar paciente',
            '5) Fin del programa'
        ]
        print('\n'.join(messages))
        msg = f"Ingrese su elección del 1 al {len(messages)}: "
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        choice = self.print_menu()
        while True:
            if choice == 1:
                spec_name = str(input("Introducir especialización: "))
                patient_name = str(input("Introducir nombre del paciente: "))
                patient_status = int(input("Ingresar estado (0 normal / 1 urgente / 2 súper urgente):  "))
                spec_exist = False
                for spec_obj in self.specs:
                    if spec_obj.name == 'Specialization ' + spec_name:
                        spec_exist = True
                if spec_exist:
                    spec_obj.add_new_patient(patient_name, patient_status)
                else:
                    new_spec = Specialization(spec_name)
                    new_spec.add_new_patient(patient_name, patient_status)
                    self.specs.append(new_spec)

            elif choice == 2:
                for spec in self.specs:
                    print(f'{spec.name}: Hay {len(spec.queue)} pacientes')
                    spec.print_patients()

            elif choice == 3:
                spec_name = str(input("Introduzca la especialización: "))
                found = False
                for spec in self.specs:
                    if spec.name == 'Specialization ' + spec_name:
                        spec.get_next_patient()
                        found = True
                if not found:
                    print("There is no Specialization with this name")

            elif choice == 4:
                spec_name = str(input("Introduzca la especialización: "))
                patient_name = str(input("Ingrese el nombre del paciente: "))
                for spec in self.specs:
                    if spec.name == 'Specialization ' + spec_name:
                        try:
                            spec.remove_patient(patient_name)
                        except:
                            print("¡Ningún paciente con tal nombre en esta especialización!")
                        spec.print_patients()

            elif choice == 5:
                break

            else:
                print("Opción no válida. Seleccione una opción válida.")
            choice = self.print_menu()