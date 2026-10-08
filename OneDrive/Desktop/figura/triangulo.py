from figura import Figura


class Triangulo(Figura):
    def __init__(
        self, base: float, altura: float, lado1: float, lado2: float
    ) -> None:
        self.validar_medidas_positivas(base, altura, lado1, lado2)
        if (
            base + lado1 <= lado2
            or base + lado2 <= lado1
            or lado1 + lado2 <= base
        ):
            raise ValueError("Las longitudes no forman un triángulo.")

        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return self.base + self.lado1 + self.lado2
