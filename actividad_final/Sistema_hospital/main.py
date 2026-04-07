from abc import ABC, abstractmethod


class Paciente(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def __str__(self):
        pass



class Medico:
    def __init__(self, especialidad):
        self.especialidad = especialidad

    def atender(self):
        return f"{self.nombre} está siendo atendido en {self.especialidad}"

class Seguro:
    def __init__(self, tipo_seguro):
        self.tipo_seguro = tipo_seguro

    def cobertura(self):
        return f"{self.nombre} tiene seguro tipo: {self.tipo_seguro}"
    
class PacienteHospital(Paciente, Medico, Seguro):
    def __init__(self, nombre, edad, especialidad, tipo_seguro, estado_salud):
        Paciente.__init__(self, nombre, edad)
        Medico.__init__(self, especialidad)
        Seguro.__init__(self, tipo_seguro)


        self._estado_salud = estado_salud

    @property
    def estado_salud(self):
        return self._estado_salud

    @estado_salud.setter
    def estado_salud(self, nuevo_estado):
        if nuevo_estado.lower() in ["estable", "critico", "grave", "recuperado"]:
            self._estado_salud = nuevo_estado
        else:
            print("Estado de salud inválido.")

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def __str__(self):
        return f"Paciente: {self.nombre}, Estado: {self._estado_salud}"



if __name__ == "__main__":
    paciente1 = PacienteHospital("Carlos", 30, "Cardiología", "Premium", "estable")
    paciente2 = PacienteHospital("Laura", 25, "Neurología", "Básico", "critico")
    paciente3 = PacienteHospital("Andrés", 40, "Pediatría", "Completo", "recuperado")

    
    print(paciente1.mostrar_info())
    print(paciente2.mostrar_info())
    print(paciente3.mostrar_info())

    print(paciente1)
    print(paciente2)
    print(paciente3)

    print("\n--- ATENCIÓN MÉDICA ---")
    print(paciente1.atender())
    print(paciente2.atender())
    print(paciente3.atender())

    print("\n--- SEGUROS ---")
    print(paciente1.cobertura())
    print(paciente2.cobertura())
    print(paciente3.cobertura())

    print("\n--- ESTADO DE SALUD ---")
    print("Paciente 1:", paciente1.estado_salud)
    print("Paciente 2:", paciente2.estado_salud)
    print("Paciente 3:", paciente3.estado_salud)

    print(f"Estado actual de {paciente1.nombre}: {paciente1.estado_salud}")

    paciente1.estado_salud = "grave"
    print(f"Nuevo estado de {paciente1.nombre}: {paciente1.estado_salud}")


    paciente1.estado_salud = "desconocido"