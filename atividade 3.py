class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def exibir_info(self):
        print(f"Monitor {self.marca}, {self.tamanho} polegadas")


class Computador:
    def __init__(self, modelo, monitor=None):
        self.modelo = modelo
        self.monitor = monitor

    def conectar_monitor(self, monitor):
        self.monitor = monitor

    def exibir_info(self):
        if self.monitor:
            print(f"Computador {self.modelo} com monitor:")
            self.monitor.exibir_info()
        else:
            print(f"Computador {self.modelo} sem monitor.")

if __name__ == "__main__":
    monitor1 = Monitor("Dell", 24)
    computador1 = Computador("Desktop 1")

    computador2 = Computador("Laptop")
    monitor2 = Monitor("Acer", 27)
    computador2.conectar_monitor(monitor2)

    computador1.exibir_info()
    computador2.exibir_info()
