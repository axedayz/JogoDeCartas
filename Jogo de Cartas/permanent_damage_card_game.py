from jogodecarta import jogodecarta
from criatura import criatura


class PermanentCardDamageGame(jogodecarta):
    def dano(self, atacante: criatura, defensor: criatura):
        self.atacante = atacante
        self.defensor = defensor
        dano_perma = self.defensor.vida - self.atacante.ataque
        return dano_perma
        