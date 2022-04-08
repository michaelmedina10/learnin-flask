class Funcionario:
    aumento = 1.04
    def __init__(self, nome, salario) :
        self.nome = nome
        self.salario = salario
        
    def dados(self):
        return {
            'Nome': self.nome,
            'Salario': self.salario
        }
    def aplicarAumento(self):
        # Usando self, pois a variável aumento será unico para cada objeto
        self.salario = self.salario * self.aumento
        
    # Criando um método que afetará cada objeto da classe
    # Atualizaremos a classe em si
    @classmethod
    def definirNovoAument(cls, novoAumento):
        cls.aumento = novoAumento
    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True
        
simone = Funcionario('Simone', 10000)
print(simone.dados())
simone.aplicarAumento()
print(simone.dados())

# Definindo um novo aumento para a CLASSE
Funcionario.definirNovoAument(1.05)
simone2 = Funcionario('Simone', 10000)
simone2.aplicarAumento()
print(simone2.dados())