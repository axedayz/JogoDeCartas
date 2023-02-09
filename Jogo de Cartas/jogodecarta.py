from abc import ABC

from criatura import criatura


class jogodecarta(ABC):
    def __init__(self, criaturas: list[criatura]) -> None:
        self.criaturas = criaturas

    def luta(self, criatura_1: criatura, criatura_2: criatura) -> criatura:
        self.dano(criatura_1, criatura_2)
        self.dano(criatura_2, criatura_1)

        primeiro_vivo: bool = criatura_1.vida > 0
        segundo_vivo: bool = criatura_2.vida > 0

        if primeiro_vivo == segundo_vivo:
            return criatura("Empate", -1, -1)

        if primeiro_vivo:
            return criatura_1
        else:
            return criatura_2

    def dano(self, atacante: criatura, defensor: criatura):
        pass
