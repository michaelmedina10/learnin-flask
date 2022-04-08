# Hello World novamente, por que não?
print('Hello World')

# FAzendo cálculos em python
a = 2
b = 3
print(a + b)

# Perguntando ao usuário
# a = int(input("Informe um valor númerico: "))
# b = int(input("Informe outro valor númerico: "))
# print(a + b)

boolean = False
if not boolean:
    print("Não é boolean")
elif boolean:
    print('E boolean')
else:
    print('não sei mais nada')
        

# Operadores lógicos or, and, not 
# Dependendo da situação você terá de usar &(and) ou |(or), queries em pandas 
# pede uma sintaze desse jeito normalmente

# métodos
def printOlaAlgumaCoisa(coisa):
    print(f'Ola {coisa}')
    
printOlaAlgumaCoisa('Jão')

def funcaoRetornaAlgo():
    a = 1
    b = 2
    return a + b

total = funcaoRetornaAlgo()
print(f'O total e {total}')

# Tuplas, listas, dicionários

a = [1,2,3,4,5,'teste',{'a':1, 'b':2, 'c': 2}]
b = {'chave1': 'dois', 'chave2': 'tres'}
c = (1,2,3,['a','b','c'])

# Lista comprehension
listaPar = list(range(1, 11, 2))
print(listaPar)
print([par ** 2 for par in listaPar if par > 3])