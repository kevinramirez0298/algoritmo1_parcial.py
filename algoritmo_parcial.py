# Clase base
class Criatura:
    def __init__(self, nombre):
        self.nombre = nombre

    def interactuar(self):
        pass


# Criatura amiga
class CriaturaAmiga(Criatura):
    def interactuar(self):
        return f"{self.nombre} te sonríe y te da un regalo mágico."


# Criatura hostil
class CriaturaHostil(Criatura):
    def interactuar(self):
        return f"{self.nombre} te ataca y pierdes 10 puntos de vida."


# Función principal del juego
def juego():
    print("Bienvenido al Bosque Encantado")

    criaturas = [
        CriaturaAmiga("un duende magico"),
        CriaturaHostil("Lobo Sombrío")
    ]

    jugando = True

    while jugando:
        print("\nAvanzas por el bosque...")
        
        # El jugador encuentra una criatura
        criatura = criaturas[0] if input("¿Quieres saber que criatura es ? (s/n): ") == "s" else criaturas[1]
        print("Te encuentras con:", criatura.nombre)

        # Interacción
        print(criatura.interactuar())

        # Decisión de continuar
        opcion = input("¿Deseas seguir explorando? (s/n): ")
        if opcion.lower() != "s":
            jugando = False

    print("Fin de la aventura.")


# Iniciar juego
juego()
