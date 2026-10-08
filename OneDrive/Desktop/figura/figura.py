import math


class Figura:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    @staticmethod
    def validar_medidas_positivas(*medidas: float) -> None:
        if any(not math.isfinite(medida) or medida <= 0 for medida in medidas):
            raise ValueError("Las medidas deben ser números finitos mayores que cero.")

    def area(self) -> float:
        raise NotImplementedError("Cada figura debe implementar su área.")

    def perimetro(self) -> float:
        raise NotImplementedError("Cada figura debe implementar su perímetro.")

    def mostrar_info(self) -> str:
        return (
            f"{self.nombre}: área = {self.area():.2f}, "
            f"perímetro = {self.perimetro():.2f}"
        )
