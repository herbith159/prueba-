import math

from figura import Figura
from hexagono import Hexagono
from rectangulo import Rectangulo
from triangulo import Triangulo


class MenuFiguras:
    """Coordina la interacción con el usuario y las figuras creadas."""

    def __init__(self) -> None:
        self.figuras: list[Figura] = []

    def _leer_numero_positivo(self, mensaje: str) -> float:
        while True:
            try:
                valor = float(input(mensaje))
            except ValueError:
                print("Ingrese un número válido.")
                continue

            if not math.isfinite(valor) or valor <= 0:
                print("La medida debe ser un número finito mayor que cero.")
                continue
            return valor

    def agregar_rectangulo(self) -> None:
        base = self._leer_numero_positivo("Base: ")
        altura = self._leer_numero_positivo("Altura: ")
        self.figuras.append(Rectangulo(base, altura))
        print("Rectángulo creado correctamente.")

    def agregar_triangulo(self) -> None:
        base = self._leer_numero_positivo("Base: ")
        altura = self._leer_numero_positivo("Altura: ")
        lado1 = self._leer_numero_positivo("Lado 1: ")
        lado2 = self._leer_numero_positivo("Lado 2: ")
        try:
            triangulo = Triangulo(base, altura, lado1, lado2)
        except ValueError as error:
            print(f"No se pudo crear el triángulo: {error}")
            return

        self.figuras.append(triangulo)
        print("Triángulo creado correctamente.")

    def agregar_hexagono(self) -> None:
        lado = self._leer_numero_positivo("Longitud del lado: ")
        apotema = self._leer_numero_positivo("Apotema: ")
        self.figuras.append(Hexagono(lado, apotema))
        print("Hexágono creado correctamente.")

    def mostrar_figuras(self) -> None:
        if not self.figuras:
            print("Todavía no se han creado figuras.")
            return

        print("\nFiguras creadas:")
        for numero, figura in enumerate(self.figuras, start=1):
            print(f"{numero}. {figura.mostrar_info()}")

    def menu_crear_figuras(self) -> None:
        while True:
            print(
                "\n--- Crear figura ---"
                "\n1. Rectángulo"
                "\n2. Triángulo"
                "\n3. Hexágono"
                "\n4. Volver al menú principal"
            )
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.agregar_rectangulo()
            elif opcion == "2":
                self.agregar_triangulo()
            elif opcion == "3":
                self.agregar_hexagono()
            elif opcion == "4":
                return
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu(self) -> None:
        while True:
            print(
                "\n=== MENÚ DE FIGURAS ==="
                "\n1. Crear figuras"
                "\n2. Mostrar figuras"
                "\n3. Salir"
            )
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.menu_crear_figuras()
            elif opcion == "2":
                self.mostrar_figuras()
            elif opcion == "3":
                print("Saliendo del programa.")
                return
            else:
                print("Opción no válida. Intente de nuevo.")
