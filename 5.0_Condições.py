# O que é if / else 
#
# if   = SE
# else = SENÃO
#
# O Python vai testar uma condição
# Se a condição for True (verdadeira):
#     → executa o bloco do if
# Se a condição for False (falsa):
#     → executa o bloco do else
#
# Apenas um dos blocos será executado
# A indentação (espaços) define o que pertence ao if ou ao else

idade = 18

if idade >= 18:
    print("Você é maior de idade\n")
else:
    # Caso contrário, ele executa o que está aqui
    print("Você é menor de idade\n")

faturamento = 1200
meta = 1000

# Verificando se a meta foi atingida
if faturamento >= meta:
    print("Meta atingida! Parabéns 🎉\n")
else:
    print("Meta não atingida 😕\n")
# faturamento >= meta

# Operadores de comparação mais usados
# ==  igual
# !=  diferente
# >   maior
# <   menor
# >=  maior ou igual
# <=  menor ou igual
#___________________________________________________________________

total_vendas_mes = 1500
meta_vendas_mes = 500

# Verifica se o total de vendas atingiu a meta
if total_vendas_mes >= meta_vendas_mes:
    print("Batemos a meta de vendas!")

    # Verifica se bateu mais que o dobro da meta
    if total_vendas_mes >= (2 * meta_vendas_mes):
        print("Foi muito fácil, batemos mais que o dobro da meta!")
    else:
        print("Passamos por pouco da meta")

else:
    # Calcula quantas vendas faltaram para bater a meta
    vendas_faltantes = meta_vendas_mes - total_vendas_mes
    print(f"Faltaram {vendas_faltantes} vendas para bater a meta")


# CADASTRO DE PRODUTOS COM if / elif / else
# Este programa simula um cadastro simples de produtos
# usando uma lista e estruturas condicionais

# Lista que armazena os produtos já cadastrados
# Todos os nomes estão em letras minúsculas para padronização
lista_produtos = ["iphone", "mac", "ipad", "airpod"]

# Mostra os produtos que já existem antes do cadastro
print("Produtos cadastrados inicialmente:")
print(lista_produtos)
#___________________________________________________________________

# ENTRADA DE DADOS

# Pede ao usuário o nome do produto que deseja cadastrar
produto_novo = input("\nDigite o nome do produto para cadastrar: ")


# Converte o texto digitado para letras minúsculas
# Isso evita erros como tratar "Iphone" e "iphone" como produtos diferentes
produto_novo = produto_novo.lower()


#___________________________________________________________________

# REGRAS DO CADASTRO (LÓGICA CONDICIONAL)
# A estrutura if / elif / else funciona assim:
#
# if   → primeira condição testada
# elif → segunda condição (só é testada se o if for falso)
# else → executa se nenhuma condição anterior for verdadeira


# Verifica se o produto já existe na lista
# O operador "in" retorna True se o item estiver na lista
if produto_novo in lista_produtos:
    # Esse bloco executa se o produto já estiver cadastrado
    print("❌ Produto já cadastrado. Nenhuma alteração foi feita.")


# Verifica se o usuário digitou um texto vazio
# Isso evita cadastrar um produto sem nome
elif produto_novo == " ":
    # Esse bloco executa se o nome estiver vazio
    print("⚠️ Nome do produto não pode ser vazio.")


# Caso nenhuma das condições acima seja verdadeira
# Ou seja: o produto NÃO existe e o nome NÃO está vazio
else:
    # Adiciona o novo produto ao final da lista
    lista_produtos.append(produto_novo)
    print("✅ Produto cadastrado com sucesso!")

#___________________________________________________________________

# RESULTADO FINAL
# Mostra a lista final após a tentativa de cadastro
print("\nLista final de produtos:")
print(lista_produtos)