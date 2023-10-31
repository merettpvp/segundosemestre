class Cabeça:
    def __init__(self):
        pass

    def mostrar_info(self):
        print("Cabeça")


class Boneco:
    def __init__(self):
        self.cabeça = Cabeça()

    def destruir(self):
        self.cabeça = None

    def mostrar_info(self):
        print("Boneco")
        if self.cabeça:
            self.cabeça.mostrar_info()
        else:
            print("Boneco destruído.")

if __name__ == "__main__":
    boneco1 = Boneco()
    boneco2 = Boneco()

    boneco1.mostrar_info()
    boneco2.mostrar_info()

    boneco1.destruir()
    boneco1.mostrar_info()