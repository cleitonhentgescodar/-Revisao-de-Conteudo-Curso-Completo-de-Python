
# FUNÇÕES EM PYTHON
# Funções servem para:
# - Organizar o código
# - Evitar repetição
# - Reaproveitar lógica
#
# Uma função é criada com a palavra-chave: def

#___________________________________________________________________

# CRIANDO UMA FUNÇÃO SIMPLES
# Essa função apenas executa um print
# Não recebe parâmetros e não retorna nada

def se_inscrever_canal():
    print("Se inscreva no canal e deixe o like!")

# Chamando (executando) a função
se_inscrever_canal()

#___________________________________________________________________

# FUNÇÃO COM PARÂMETRO E RETORNO
# Essa função recebe um preço e calcula um novo preço
# aplicando inflação + imposto (ISS)

def calcular_novo_preco(preco):
    inflacao = 0.05   # 5%
    iss = 0.07        # 7%

    novo_preco = preco * (1 + inflacao + iss)

    # round(valor, casas_decimais)
    return round(novo_preco, 2)

#___________________________________________________________________

# USANDO FUNÇÃO COM DICIONÁRIO + FOR
# Dicionário com produtos e preços originais

dic_produtos = {
    "iphone": 10000,
    "mac": 15000,
    "apple watch": 5000,
    "airpod": 2000
}

print("\nPreços originais:")
print(dic_produtos)


# Percorrendo o dicionário
# item = chave (nome do produto)

for item in dic_produtos:
    preco_original = dic_produtos[item]

    # chamando a função e passando o preço
    novo_preco = calcular_novo_preco(preco_original)

    # atualizando o valor no dicionário
    dic_produtos[item] = novo_preco


print("\nPreços após reajuste:")
print(dic_produtos)