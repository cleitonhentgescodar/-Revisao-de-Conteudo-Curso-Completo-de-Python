# input sempre retorna uma string
faturamento = input("Digite o faturamento desse mês (ex: R$800 ou 800): ")

# remove símbolo de moeda, espaços e troca vírgula por ponto
faturamento = faturamento.replace("R$", "").replace(" ", "").replace(",", ".")

# converte para número
faturamento = float(faturamento)

custo = 300

# cálculo do lucro
lucro = faturamento - custo

# saída formatada com 2 casas decimais
print(f"O faturamento foi de R${faturamento:.2f} e o lucro foi de R${lucro:.2f}")