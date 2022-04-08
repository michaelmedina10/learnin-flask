# args => argumentos
# kwargs => keywords arguments (Argumentos de palavrs-chave)

# *args aceita quantos argumentos eu queira passar
def soma_simplificada(*args):
    return sum(args)

print(soma_simplificada(1,2,3,4,5,6))

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    
metodo_kwargs(1,2,3, 'teste', nome='teste2', idade='nao sei')