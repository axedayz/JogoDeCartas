from criatura import criatura
from permanent_damage_card_game import PermanentCardDamageGame
from temporary_damage_card_game import TemporaryCardDamageGame

criatura_pikachu = criatura("Pikachu", 25, 40)
criatura_dragonite = criatura("Dragonite", 10, 25)

criaturas: list[criatura] = []

criaturas.append(criatura_pikachu)
criaturas.append(criatura_dragonite)


permanent_damage_card_game = PermanentCardDamageGame(criaturas)

primeiro_round = permanent_damage_card_game.luta(criatura_pikachu, criatura_dragonite)
print(primeiro_round.nome)
segundo_round = permanent_damage_card_game.luta(criatura_pikachu, criatura_dragonite)
print(segundo_round.nome)