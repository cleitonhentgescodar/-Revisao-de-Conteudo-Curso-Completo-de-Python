# Variáveis

faturamento = 1000
custo = 300
imposto = 0.2
lucro1 = faturamento - custo - imposto * faturamento

faturamento = 600
lucro2 = faturamento - custo - imposto * faturamento

print(lucro1)
print(lucro2)

# Tipos de Variáveis
# Int --> Numeros inteiros
# float --> Numeros com casas decimais.
# String --> Textos 
# Boleanos --> verdadeiro ou falso (True / False)

print("O lucro da loja no primeiro mês foi de", lucro1)
print("O lucro da loja no segundo mês foi de", lucro2 )
print("\n")
print("O lucro da loja foi de:", lucro1, "para o primeiro mês\n")


margem_lucro = lucro2 / faturamento
print("Margem de lucro de:", margem_lucro)

#  Retorna True 
meta = 0.2
bateu_meta = margem_lucro >= meta  # booleano
print(bateu_meta)

# Retorna False 
meta = 0.5
bateu_meta = margem_lucro >= meta  # booleano
print(bateu_meta,"\n")

# mod % (resto da divisão)
# // (parte inteira da divisão)

duracao_contrato = 140  # meses

anos = duracao_contrato // 12
meses_sobra = duracao_contrato % 12

print("O contrato tem", anos, "anos e", meses_sobra, "meses")