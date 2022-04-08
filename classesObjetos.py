# Classe
class JogadorLoteria:
    # Construtor
    def __init__(self):
        self.nome = "Michael"
        self.numeros = (13, 4, 52, 23, 67, 82)
        
    def total(self):
        return sum(self.numeros)
    
jogador1 = JogadorLoteria()
jogador2 = JogadorLoteria()

print(jogador1.total())
print(jogador2.total())
print(jogador1 == jogador2)
print(type(jogador1))