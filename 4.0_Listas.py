# LISTAS EM PYTHON
# Listas servem para armazenar vários valores em uma única variável
# Os valores ficam entre colchetes [ ]
# Cada item tem uma posição (índice), que começa em 0

lista_presidentes = ["Lula", "Bolsonaro", "Temer", "Dilma", "FHC"]
print("Lista inicial de presidentes:", lista_presidentes)

#___________________________________________________________________

# TAMANHO DA LISTA
# len() retorna quantos elementos existem na lista
print("\nQuantidade de presidentes na lista:")
print(len(lista_presidentes))

#___________________________________________________________________

# ACESSANDO ELEMENTOS DA LISTA
print("\nAcessando elementos da lista:")

# primeiro elemento (índice 0)
primeiro = lista_presidentes[0]
print("Primeiro presidente da lista:", primeiro)

# segundo elemento (índice 1)
segundo = lista_presidentes[1]
print("Segundo presidente da lista:", segundo)

# último elemento (índice -1)
ultimo = lista_presidentes[-1]
print("Último presidente da lista:", ultimo)

#___________________________________________________________________

# VERIFICAR SE UM ITEM EXISTE NA LISTA
print("\nVerificando se nomes existem na lista:")

existe_lula = "Lula" in lista_presidentes
print("Lula está na lista?", existe_lula)

existe_sarney = "Sarney" in lista_presidentes
print("Sarney está na lista?", existe_sarney)

#___________________________________________________________________

# ADICIONAR ELEMENTOS NA LISTA
print("\nAdicionando um novo presidente à lista:")
lista_presidentes.append("Sarney")
print("Lista após adicionar Sarney:", lista_presidentes)

#___________________________________________________________________

# REMOVER ELEMENTOS DA LISTA
print("\nRemovendo um presidente da lista:")
lista_presidentes.remove("Temer")
print("Lista após remover Temer:", lista_presidentes)

#___________________________________________________________________

# ORDENAR A LISTA
print("\nOrdenando a lista em ordem alfabética:")
lista_presidentes.sort()
print("Lista ordenada:", lista_presidentes)

#___________________________________________________________________

# PERCORRER A LISTA (loop)
print("\nPercorrendo a lista de presidentes:")
for presidente in lista_presidentes:
    print("Presidente:", presidente)

#___________________________________________________________________

# EXEMPLO DE ÍNDICES EM LISTAS
# Cada item da lista tem um índice (posição)
# O índice sempre começa em 0

lista_presidentes = ["Lula", "Bolsonaro", "Temer", "Dilma", "FHC"]

print("Lista completa:", lista_presidentes)

print("\nÍndices e valores da lista:")

# mostrando índice e valor juntos
for index, presidente in enumerate(lista_presidentes):
    print(f"Índice {index} -> {presidente}")


# acessando diretamente pelo índice
print("\nAcessando itens pelo índice:")

print("Item no índice 0:", lista_presidentes[0])   # primeiro
print("Item no índice 2:", lista_presidentes[2])   # terceiro
print("Item no índice -1:", lista_presidentes[-1]) # último

#___________________________________________________________________
# LISTAS NUMÉRICAS EM PYTHON
# Listas numéricas armazenam valores do tipo int ou float
# Cada número tem um índice (posição) que começa em 0

lista_vendas = [100, 250, 300, 150, 400]

print("Lista inicial de vendas:", lista_vendas)


#___________________________________________________________________
# TAMANHO DA LISTA
print("\nQuantidade de valores na lista:")
print(len(lista_vendas))

#___________________________________________________________________
# ACESSANDO VALORES PELO ÍNDICE
print("\nAcessando valores pelo índice:")

print("Primeiro valor (índice 0):", lista_vendas[0])
print("Terceiro valor (índice 2):", lista_vendas[2])
print("Último valor (índice -1):", lista_vendas[-1])

#___________________________________________________________________
# SOMA DOS VALORES DA LISTA
# sum() soma todos os números da lista
print("\nSomando todos os valores da lista:")
total_vendas = sum(lista_vendas)
print("Total de vendas:", total_vendas)

#___________________________________________________________________
# MAIOR E MENOR VALOR
# max() retorna o maior número
# min() retorna o menor número
print("\nMaior e menor valor da lista:")
print("Maior venda:", max(lista_vendas))
print("Menor venda:", min(lista_vendas))

#___________________________________________________________________
# MÉDIA DOS VALORES
# média = soma / quantidade
print("\nMédia de vendas:")
media_vendas = sum(lista_vendas) / len(lista_vendas)
print("Média de vendas:", media_vendas)

#___________________________________________________________________
# ALTERANDO UM VALOR PELO ÍNDICE
print("\nAlterando um valor da lista:")

lista_vendas[1] = 280  # altera o valor no índice 1
print("Lista após alteração:", lista_vendas)

#___________________________________________________________________
# ORDENANDO A LISTA
print("\nOrdenando a lista de vendas:")
lista_vendas.sort()
print("Lista ordenada:", lista_vendas)

#___________________________________________________________________
# PERCORRENDO A LISTA COM ÍNDICE
print("\nPercorrendo a lista com índice e valor:")

for index, valor in enumerate(lista_vendas):
    print(f"Índice {index} -> Valor {valor}")

#___________________________________________________________________
# FUNÇÕES PARA TRABALHAR COM LISTAS
# Funções ajudam a organizar o código
# Evitam repetição e deixam tudo mais legível

def mostrar_lista(lista, nome_lista):
    """
    Mostra a lista completa no terminal
    """
    print(f"\nLista {nome_lista}: {lista}")


def tamanho_lista(lista):
    """
    Retorna o tamanho da lista usando len()
    """
    print("\nQuantidade de itens na lista:")
    print(len(lista))


def acessar_itens(lista):
    """
    Mostra exemplos de acesso por índice
    """
    print("\nAcessando itens da lista por índice:")
    print("Primeiro item (índice 0):", lista[0])
    print("Último item (índice -1):", lista[-1])


def verificar_item(lista, item):
    """
    Verifica se um item existe na lista
    Retorna True ou False
    """
    print(f"\nVerificando se '{item}' está na lista:")
    print(item in lista)


def adicionar_item(lista, item):
    """
    Adiciona um item no final da lista
    """
    print(f"\nAdicionando '{item}' à lista:")
    lista.append(item)
    print(lista)


def remover_item(lista, item):
    """
    Remove um item da lista pelo valor
    """
    print(f"\nRemovendo '{item}' da lista:")
    if item in lista:
        lista.remove(item)
        print(lista)
    else:
        print("Item não encontrado na lista.")


def ordenar_lista(lista):
    """
    Ordena a lista em ordem crescente (alfabética ou numérica)
    """
    print("\nOrdenando a lista:")
    lista.sort()
    print(lista)


def percorrer_lista(lista):
    """
    Percorre a lista mostrando índice e valor
    """
    print("\nPercorrendo a lista com índice e valor:")
    for index, valor in enumerate(lista):
        print(f"Índice {index} -> {valor}")

# USANDO AS FUNÇÕES – LISTA DE PRESIDENTES

lista_presidentes = ["Lula", "Bolsonaro", "Temer", "Dilma", "FHC"]

mostrar_lista(lista_presidentes, "Presidentes")
tamanho_lista(lista_presidentes)
acessar_itens(lista_presidentes)
verificar_item(lista_presidentes, "Lula")
verificar_item(lista_presidentes, "Sarney")
adicionar_item(lista_presidentes, "Sarney")
remover_item(lista_presidentes, "Temer")
ordenar_lista(lista_presidentes)
percorrer_lista(lista_presidentes)

# USANDO AS FUNÇÕES – LISTA NUMÉRICA

lista_vendas = [100, 250, 300, 150, 400]

mostrar_lista(lista_vendas, "Vendas")
tamanho_lista(lista_vendas)
acessar_itens(lista_vendas)
ordenar_lista(lista_vendas)
percorrer_lista(lista_vendas)
