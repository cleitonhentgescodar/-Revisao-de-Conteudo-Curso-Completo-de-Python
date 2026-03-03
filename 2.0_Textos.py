faturamento = 1000
custo = 300

lucro = faturamento - custo

print("O lucro foi de:", lucro, "e o faturamento foi de:", faturamento)

mensagem = "O lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)
print(mensagem)

# f-string (formatted string)
# Serve para criar textos dinâmicos, misturando texto com variáveis
# Usamos a letra f antes das aspas
# As variáveis ficam dentro de { } e são substituídas pelo valor automaticamente
# É a forma mais simples, limpa e recomendada de trabalhar com textos em Python

texto = f"O lucro foi de {lucro} e o faturamento foi de {faturamento}"
print(texto)

# fórmulas/funções de texto
email = "EMAIL_FALSO_DO_LULA@gmail.com"

email = email.lower()  # coloca em letra minúscula
email = email.upper()  # coloca em letra maiúscula

print(email)

# tamanho de um texto
tamanho_texto = len(email)
print(tamanho_texto)

# posição de um caractere no texto
posicao = email.find("@")
print(posicao)

# pedaços de um texto (fatiamento / slicing)
nome_usuario = email[:posicao]
print(nome_usuario)

# trocar um pedaço de texto
email = email.lower()
email = email.replace("gmail.com", "yahoo.com")
print(email)

# title, capitalize, upper
nome = "luiz inácio"

print(nome.capitalize())  # coloca a 1ª letra maiúscula
print(nome.title())       # coloca a 1ª letra de cada palavra maiúscula
print(nome.upper())       # coloca tudo maiúsculo
print(nome)