# 🌲 Videojuego: Bosque Encantado  
### Primera versión — Interacción con criaturas usando Python

---

## 📌 Descripción del proyecto

Este proyecto es la primera versión de un videojuego ambientado en un **bosque encantado**, donde el jugador avanza por diferentes zonas y se encuentra con criaturas mágicas.  
El recorrido del bosque se controla mediante **ciclos**, las criaturas se modelan con **clases y herencia**, y las decisiones del jugador se gestionan con **condicionales**.

El objetivo es permitir interacciones básicas con criaturas amigables y hostiles.

---

## 🎯 Requerimientos Funcionales

### ✔️ 1. Recorrer el bosque
El jugador debe avanzar en el bosque usando ciclos (bucles) que mantengan el juego activo mientras desee continuar.

### ✔️ 2. Interacción con criaturas
El sistema debe permitir que el jugador se encuentre e interactúe con al menos dos tipos de criaturas:
- Criatura amiga  
- Criatura hostil  

### ✔️ 3. Uso de clases y herencia
Las criaturas deben derivarse de una **clase base común**, compartiendo características esenciales y comportamientos iniciales.

### ✔️ 4. Toma de decisiones
El jugador debe poder elegir acciones que influyen en el desarrollo del juego.  
Estas decisiones deben evaluarse mediante **condicionales (`if`)**.

### ✔️ 5. Comportamientos de criaturas
Cada criatura debe tener respuestas únicas:
- Las criaturas amigables ayudan al jugador.
- Las criaturas hostiles afectan negativamente su progreso.

---

## 🧩 Código en Python

```python
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
        CriaturaAmiga("Hada Brillante"),
        CriaturaHostil("Lobo Sombrío")
    ]

    jugando = True

    while jugando:
        print("\nAvanzas por el bosque...")
        
        # El jugador encuentra una criatura
        criatura = criaturas[0] if input("¿Quieres una criatura amiga? (s/n): ") == "s" else criaturas[1]
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
