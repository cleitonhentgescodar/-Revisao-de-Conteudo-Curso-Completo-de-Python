
# ESTRUTURA DE REPETIÇÃO FOR EM PYTHON
# O for é usado quando queremos repetir uma ação
# para cada item de uma sequência (lista, range, etc)
# ==================================================

#___________________________________________________________________
# EXEMPLO 1 - FOR PERCORRENDO UMA LISTA

# Temos uma lista de produtos
lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

print("Lista de produtos:")

# O for vai passar por CADA item da lista
for item in lista_produtos:
    print("Produto:", item)

# Explicação:
# 1) O for pega um item da lista por vez
# 2) Cada item é guardado na variável 'item'
# 3) O bloco indentado é executado para cada item

#___________________________________________________________________
# EXEMPLO 2 - FOR COM INTERVALO FIXO (range)
# range(10) cria uma sequência de números de 0 até 9

print("\nContando de 0 até 9:")

for i in range(10):
    print("Número:", i)

# Explicação:
# range(10) → 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# A variável 'i' muda a cada repetição

#___________________________________________________________________
# EXEMPLO 3 - FOR COM INÍCIO E FIM DEFINIDOS
# range(inicio, fim)
# O fim NÃO é incluído

print("\nContando de 1 até 5:")

for i in range(1, 6):
    print("Número:", i)

#___________________________________________________________________
# EXEMPLO 4 - FOR COM ÍNDICE (enumerate)
# enumerate() permite acessar o índice e o valor

print("\nProdutos com índice:")

for indice, produto in enumerate(lista_produtos):
    print(f"Índice {indice} -> Produto {produto}")

# Explicação:
# indice → posição do item na lista
# produto → valor armazenado naquela posição

#___________________________________________________________________

# EXEMPLOS DE USO DO FOR EM PYTHON

# for item in lista
# Use quando quiser passar por cada elemento da lista

lista_nomes = ["Ana", "Bruno", "Carlos", "Daniela"]

print("Percorrendo cada nome da lista:")

for nome in lista_nomes:
    print("Nome:", nome)

# Explicação:
# O for pega um nome por vez da lista
# A variável 'nome' recebe cada elemento


# for i in range()
# Use quando quiser repetir algo um número fixo de vezes

print("\nRepetindo uma ação 5 vezes:")

for i in range(5):
    print("Repetição número:", i)

# Explicação:
# range(5) gera os números: 0, 1, 2, 3, 4
# O código dentro do for executa 5 vezes


# enumerate()
# Use quando precisar do índice + valor ao mesmo tempo

print("\nUsando enumerate para mostrar índice e valor:")

for indice, nome in enumerate(lista_nomes):
    print(f"Índice {indice} -> Nome {nome}")

# Explicação:
# enumerate() devolve:
# - indice → posição do item na lista
# - nome → valor armazenado nessa posição