# COLEÇÕES
# -----------------------------------------------------------------------------------------------------------------------
# Tupla ()
nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes)

# Slicing de dados primero dado "picotar dados para extrair apenas o desejado"
print(nomes[0])

# Slicing de dados ate 'Trunks'
print(nomes[:2])

# Slicing de dados 'Vegeta' e 'Trunks' [inclusive:exclusive]
print(nomes[1:3])

# Slicing de dados negativo
print(nomes[-2])

# TypeError: 'tuple' object does not support item assignment (Coleção imutável)
nomes[0] = 'Picolo'

# -----------------------------------------------------------------------------------------------------------------------
# Listas []
nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# Inserido elementos em uma lista
nomes.append('Picolo')

# Atualizad elementos em uma lista
nomes[0] = ('Bulma')

# Deletando elementos de uma lista
nomes.remove('Trunks')  # Por valor
del nomes[1]  # Por índice

# Mostrando elementos de uma lista
print(nomes)

# -----------------------------------------------------------------------------------------------------------------------
# Conjunto (set) {}
nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}

# Adicionando elementos em um conjunto (nao apresenta ordem)
nomes.add('Bulma')

# Não se adiciona elemetos repetidos
nomes.add('Goku')

# Remover eementos de um conjuntos
nomes.remove('Trunks')

# Conjuntos NÃO GUARDAM ELEMENTOS REPETIDOS a ordem dos elementos inseridos
print(nomes)

# Não possui Update

# -----------------------------------------------------------------------------------------------------------------------
# Dicionario {} (identico a um JSON)
pessoa = {
    'nome': 'Goku',
    'idade': 42
}

pessoa2 = {
    'nome': 'Bulma',
    'idade': 32
}

# Coleção dentro de coleção
pessoas = [pessoa, pessoa2]

# Mostrando elementos de uma lista (pessoa[Goku]['nome])
print(pessoas[0]['nome'])

# Inserindo elementos em um dicionario
pessoa['sexo'] = 'M'

# Deletando elementos de uma lista
del pessoa['idade']

# Atualizado itens em um disiconario
pessoa['nome'] = 'Gohan'

# Mostrando todos os dados de um dicionario
print(pessoas[0])

# -----------------------------------------------------------------------------------------------------------------------
