
# LISTAS EM PYTHON (usando duas listas relacionadas / Dicionário)
# Uma lista guarda os nomes dos produtos
# Outra lista guarda os preços
# O relacionamento é feito PELO ÍNDICE

# Lista de produtos
lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

# Lista de preços (cada preço corresponde ao produto do MESMO índice)
lista_precos = [10000, 15000, 5000, 2000]

print("Listas iniciais:")
print("Produtos:", lista_produtos)
print("Preços:", lista_precos)


#___________________________________________________________________
# ACESSAR UM VALOR USANDO O ÍNDICE
# Para acessar o preço do iPhone, usamos o índice do iPhone
indice_iphone = lista_produtos.index("iphone")
preco_iphone = lista_precos[indice_iphone]

print("\nPreço do iPhone:")
print(preco_iphone)


#___________________________________________________________________
# EDITAR UM VALOR EXISTENTE
# Aumentando o preço do Mac em 10%

indice_mac = lista_produtos.index("mac")
lista_precos[indice_mac] = lista_precos[indice_mac] * 1.1

print("\nListas após aumentar o preço do Mac em 10%:")
print("Produtos:", lista_produtos)
print("Preços:", lista_precos)


#___________________________________________________________________
# ADICIONAR UM NOVO ITEM
# É MUITO IMPORTANTE adicionar nas DUAS listas

lista_produtos.append("apple tv")
lista_precos.append(14000)

print("\nListas após adicionar o Apple TV:")
print("Produtos:", lista_produtos)
print("Preços:", lista_precos)


#___________________________________________________________________
# REMOVER UM ITEM
# Primeiro encontramos o índice e removemos das DUAS listas

indice_mac = lista_produtos.index("mac")

lista_produtos.pop(indice_mac)
lista_precos.pop(indice_mac)

print("\nListas após remover o Mac:")
print("Produtos:", lista_produtos)
print("Preços:", lista_precos)


#___________________________________________________________________
# VERIFICAR SE UM PRODUTO EXISTE NA LISTA

print("\nVerificando se o produto 'mac' existe:")
if "mac" in lista_produtos:
    print("Produto encontrado")
else:
    print("Produto não encontrado")

print("\nVerificando se o produto 'iphone' existe:")
if "iphone" in lista_produtos:
    print("Produto encontrado")
else:
    print("Produto não encontrado")

#___________________________________________________________________
# TRANSFORMANDO DUAS LISTAS EM UM DICIONÁRIO
# Vamos usar:
# 1) uma lista de produtos
# 2) uma lista de preços
# Depois vamos unir as duas em um dicionário
#___________________________________________________________________

# Lista com nomes dos produtos
lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

# Lista com os preços dos produtos
# A ORDEM é MUITO IMPORTANTE
# Cada preço corresponde ao produto do MESMO índice
lista_precos = [10000, 15000, 5000, 2000]

print("Lista de produtos:", lista_produtos)
print("Lista de preços:", lista_precos)

#___________________________________________________________________
# USANDO zip()
# zip() junta elementos de listas diferentes pelo índice
#
# Exemplo do zip:
# ("iphone", 10000)
# ("mac", 15000)
# ("apple watch", 5000)
# ("airpod", 2000)
#
#___________________________________________________________________

pares_produto_preco = zip(lista_produtos, lista_precos)
print("\nResultado do zip:")
print(list(pares_produto_preco))

#___________________________________________________________________
# TRANSFORMANDO EM DICIONÁRIO
# dict() converte os pares (chave, valor) em dicionário
novo_dicionario = dict(zip(lista_produtos, lista_precos))

print("\nDicionário criado a partir das listas:")
print(novo_dicionario)