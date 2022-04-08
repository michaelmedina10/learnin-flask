class Funcionario:
    def __init__(self, nome, salario) :
        self.nome = nome
        self.salario = salario
        
    def dados(self):
        return {
            'Nome': self.nome,
            'Salario': self.salario
        }
        
funcionario1 = Funcionario('Michael', '5000.00')
print(funcionario1.nome)
print(funcionario1.salario)
print(funcionario1.dados())

# Usando a Herança

class Administrador(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        
    def atualizarSalario(self, salario):
        self.salario = salario
        return self.dados()
    
admin1 = Administrador('Michael', 8000)
print(admin1.dados())
admin1.atualizarSalario(12000)
print(admin1.dados())
        
