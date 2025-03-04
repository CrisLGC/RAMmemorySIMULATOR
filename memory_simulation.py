class Proceso:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def __repr__(self):
        return f"{self.nombre} ({self.tamaño} MB)"


class MemoriaRAM:
    def __init__(self, tamaño_total):
        self.tamaño_total = tamaño_total
        self.memoria_disponible = tamaño_total
        self.procesos = []

    def asignar_memoria(self, proceso):

        if proceso.tamaño <= 0:
            print("Error: El tamaño del proceso debe ser un número entero positivo.")
            return

        if proceso.tamaño > self.memoria_disponible:
            print(f"Error: No hay suficiente memoria disponible para {proceso.nombre}")
            return

        # Implementación de la política de asignación "Best Fit"
        espacios_disponibles = self._obtener_espacios_disponibles()
        mejor_ajuste = None

        for espacio in espacios_disponibles:
            if espacio >= proceso.tamaño and (mejor_ajuste is None or espacio < mejor_ajuste):
                mejor_ajuste = espacio

        if mejor_ajuste is None:
            print(f"Error: No se encontró un espacio adecuado para {proceso.nombre}")
            return

        self.procesos.append(proceso)
        self.memoria_disponible -= proceso.tamaño
        print(f"Memoria asignada a {proceso.nombre}")

    def desasignar_memoria(self, nombre_proceso):

        proceso_a_eliminar = None
        for proceso in self.procesos:
            if proceso.nombre == nombre_proceso:
                proceso_a_eliminar = proceso
                break

        if proceso_a_eliminar is None:
            print(f"Error: No se encontró el proceso {nombre_proceso}")
            return

        self.procesos.remove(proceso_a_eliminar)
        self.memoria_disponible += proceso_a_eliminar.tamaño
        print(f"Memoria desasignada de {nombre_proceso}")

    def mostrar_estado_memoria(self):
        print("\nEstado de la Memoria RAM:")
        print(f"Memoria Total: {self.tamaño_total} MB")
        print(f"Memoria Disponible: {self.memoria_disponible} MB")
        print("Procesos Activos:")
        for proceso in self.procesos:
            print(f"  - {proceso}")
        print()

    def _obtener_espacios_disponibles(self):
        espacios_disponibles = [self.memoria_disponible]
        return espacios_disponibles


def main():
    memoria = MemoriaRAM(1024)  # Memoria RAM de 1024 MB

    while True:
        print("1. Crear nuevo proceso")
        print("2. Asignar memoria a proceso")
        print("3. Desasignar memoria de proceso")
        print("4. Ver estado actual de la memoria")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del proceso: ")
            tamaño = input("Ingrese el tamaño de memoria requerido (MB): ")

            if not tamaño.isdigit() or int(tamaño) <= 0:
                print("Error: El tamaño de memoria debe ser un número entero positivo.")
                continue

            tamaño = int(tamaño)
            proceso = Proceso(nombre, tamaño)
            memoria.asignar_memoria(proceso)
        elif opcion == "2":
            if len(memoria.procesos) == 0:
                print("Error: No hay procesos activos a los que se pueda asignar memoria.")
                continue

            nombre = input("Ingrese el nombre del proceso a asignar memoria: ")
            tamaño = input("Ingrese el tamaño de memoria requerido (MB): ")

            if not tamaño.isdigit() or int(tamaño) <= 0:
                print("Error: El tamaño de memoria debe ser un número entero positivo.")
                continue

            tamaño = int(tamaño)
            proceso = Proceso(nombre, tamaño)
            memoria.asignar_memoria(proceso)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del proceso a desasignar memoria: ")
            memoria.desasignar_memoria(nombre)
        elif opcion == "4":
            memoria.mostrar_estado_memoria()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
