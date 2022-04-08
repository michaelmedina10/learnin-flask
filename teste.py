import json
hoteis = [
    
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.3,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.3,
        'diaria': 420.3,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 4.3,
        'diaria': 420.3,
        'cidade': 'Santa Catarina'
    },
]

hoteis[1].update({
        'nome': 'Bravo Atualizado Hotel',
        'estrelas': 4.3,
        'diaria': 420.3,
        'cidade': 'São Paulo'}) 

print(hoteis)
 
 
dados = {'limit': 50, 'offset': None, 'cidade': 'Sao Paulo'}

teste = {chave: dados[chave] for chave in dados.keys() if dados[chave] is not None}
print(f'Teste {teste}')
print(tuple([value for value in teste.values()]))
print(tuple(teste.values()))