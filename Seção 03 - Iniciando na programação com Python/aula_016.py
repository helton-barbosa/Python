# if -> se
# elif -> senão se
# else -> senão

# Para realizar os testes de condição verdaeira ou falsa, utiliza-se de
# condições de comparação >, >=, <, <=, == e !=

# A estrutura if é a forma mais simples de controle de fluxo. Ele executa um
# bloco de código apenas se uma determinada condição for verdadeira (True).
# Sintaxe:
"""
if condicao:
    Bloco de código a ser executado se a condição for verdadeira.

condicao - é uma expressão que o Python avalia como True ou False
""" 
print('if')
idade = 19

if idade >= 18:
    print("Você tem idade suficiente para votar!")
    print("Já fez seu registro eleitoral?")

# A estrutura if-else utiliza-se quando se quer que o programa faça algo
# quando a condição é verdadeira e faça outra coisa se a condição for falsa.
# Sintaxe:
"""
if condicao:
    # Bloco executado se a condição for True
else:
    # Bloco executado se a condição for False
"""
print('\nif - else')
idade = 17

if idade >= 18:
    print("Você tem idade suficiente para votar!")
else:
    print("Desculpe, você ainda não pode votar.")
    print("Por favor, registre-se assim que fizer 18 anos!")

# A estrutura if-elif-else é usada para testar mais de duas situações. O Python
# executa cada teste condicional em ordem até que um deles passe. Quando um
# teste passa, o código dentro daquele bloco é executado, e o Python ignora o
# resto da cadeia.
# Sintaxe:
"""
if condicao_1:
    # Bloco executado se a condicao_1 for True
elif condicao_2:
    # Bloco executado se a condicao_1 for False e a condicao_2 for True
else:
    # Bloco executado se todas as condições anteriores forem False
"""
print('\nif - elif - else')
idade = 12

if idade < 4:
    preco = 0
elif idade < 18:
    preco = 25
else:
    preco = 40

print(f"O seu ingresso custa R${preco},00.")
