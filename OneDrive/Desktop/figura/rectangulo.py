from figura import Figura


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float) -> None:
        self.validar_medidas_positivas(base, altura)
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)
