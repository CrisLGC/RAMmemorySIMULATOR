import time
import random
from collections import OrderedDict
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class RAM:
    def __init__(self, size):
        # Inicializamos la memoria con un tamaño específico
        self.size = size
        self.memory = [0] * size  # Cada celda de memoria se inicializa a 0

    def read(self, address):
        # Simulamos un retardo de acceso a la RAM (100 ns)
        time.sleep(0.0001)  # 100 ns
        if 0 <= address < self.size:
            return self.memory[address]
        else:
            raise IndexError(f"Dirección de memoria {address} fuera de rango (0-{self.size - 1})")

    def write(self, address, value):
        # Simulamos un retardo de acceso a la RAM (100 ns)
        time.sleep(0.0001)  # 100 ns
        if 0 <= address < self.size:
            self.memory[address] = value
        else:
            raise IndexError(f"Dirección de memoria {address} fuera de rango (0-{self.size - 1})")

    def clear(self):
        # Limpiamos toda la memoria (establecemos todas las celdas a 0)
        self.memory = [0] * self.size

    def __str__(self):
        # Representación de la memoria para facilitar la visualización
        return str(self.memory)

class Cache:
    def __init__(self, ram, cache_size):
        # Inicializamos la caché con un tamaño específico
        self.ram = ram
        self.cache_size = cache_size
        self.cache = OrderedDict()  # Usamos OrderedDict para implementar LRU

    def read(self, address):
        # Simulamos un retardo de acceso a la caché (10 ns)
        time.sleep(0.00001)  # 10 ns
        if address in self.cache:
            print(f"Cache hit para la dirección {address}")
            # Movemos la dirección al final para indicar que fue usada recientemente
            self.cache.move_to_end(address)
            return self.cache[address]
        else:
            print(f"Cache miss para la dirección {address}")
            value = self.ram.read(address)
            self.cache[address] = value
            if len(self.cache) > self.cache_size:
                # Eliminamos la entrada menos recientemente usada (LRU)
                self.cache.popitem(last=False)
            return value

    def write(self, address, value):
        # Simulamos un retardo de acceso a la caché (10 ns)
        time.sleep(0.00001)  # 10 ns
        self.cache[address] = value
        self.ram.write(address, value)
        if len(self.cache) > self.cache_size:
            # Eliminamos la entrada menos recientemente usada (LRU)
            self.cache.popitem(last=False)

    def clear_cache(self):
        # Limpiamos la caché
        self.cache.clear()

def visualize_memory(ram, ax):
    # Visualizamos el estado de la memoria en un gráfico de barras
    ax.clear()
    ax.bar(range(ram.size), ram.memory, color='blue')
    ax.set_xlabel('Dirección de Memoria')
    ax.set_ylabel('Valor')
    ax.set_title('Estado de la Memoria RAM')
    ax.set_ylim(0, max(ram.memory) + 10 if max(ram.memory) > 0 else 10)

class MemorySimulatorApp:
    def __init__(self, root, ram, cache):
        self.root = root
        self.ram = ram
        self.cache = cache

        # Configuración de la ventana
        self.root.title("Simulador de Memoria RAM y Caché")

        # Crear un gráfico de matplotlib
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Botones y entradas
        self.address_label = tk.Label(root, text="Dirección de Memoria:")
        self.address_label.pack()
        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        self.value_label = tk.Label(root, text="Valor:")
        self.value_label.pack()
        self.value_entry = tk.Entry(root)
        self.value_entry.pack()

        self.read_button = tk.Button(root, text="Leer", command=self.read_memory)
        self.read_button.pack()

        self.write_button = tk.Button(root, text="Escribir", command=self.write_memory)
        self.write_button.pack()

        self.clear_button = tk.Button(root, text="Limpiar Memoria", command=self.clear_memory)
        self.clear_button.pack()

        # Actualizar la visualización inicial
        self.update_visualization()

    def read_memory(self):
        try:
            address = int(self.address_entry.get())
            value = self.cache.read(address)
            print(f"Valor en la dirección {address}: {value}")
        except ValueError:
            print("Error: La dirección debe ser un número entero.")
        except IndexError as e:
            print(e)
        self.update_visualization()

    def write_memory(self):
        try:
            address = int(self.address_entry.get())
            value = int(self.value_entry.get())
            self.cache.write(address, value)
            print(f"Valor {value} escrito en la dirección {address}.")
        except ValueError:
            print("Error: La dirección y el valor deben ser números enteros.")
        except IndexError as e:
            print(e)
        self.update_visualization()

    def clear_memory(self):
        self.ram.clear()
        self.cache.clear_cache()
        print("Memoria RAM y caché limpiadas.")
        self.update_visualization()

    def update_visualization(self):
        visualize_memory(self.ram, self.ax)
        self.canvas.draw()

# Ejecución del programa
if __name__ == "__main__":
    # Creamos una RAM con 32 celdas de memoria
    ram = RAM(32)

    # Creamos una caché con un tamaño de 8 celdas
    cache = Cache(ram, 8)

    # Iniciamos la interfaz gráfica
    root = tk.Tk()
    app = MemorySimulatorApp(root, ram, cache)
    root.mainloop()