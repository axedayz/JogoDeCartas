from jogodecarta import jogodecarta
from criatura import criatura


class TemporaryCardDamageGame(jogodecarta):
    def dano(self, atacante: criatura, defensor: criatura) -> int: 
        self.atacante = atacante
        self.defensor = defensor
        dano_rodada = self.defensor.vida - self.atacante.ataque
        return dano_rodada
        