from figura import Figura


class Hexagono(Figura):
    def __init__(self, lado: float, apotema: float) -> None:
        self.validar_medidas_positivas(lado, apotema)
        super().__init__("Hexágono regular")
        self.lado = lado
        self.apotema = apotema

    def area(self) -> float:
        return (self.perimetro() * self.apotema) / 2

    def perimetro(self) -> float:
        return 6 * self.lado
