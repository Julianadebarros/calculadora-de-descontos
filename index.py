# Essa é uma calculadora de descontos
print("Essa é a calculadora de descontos!")
# Pedir valor da compra e porcentagem em desconto
valor_da_compra = input("O valor total da compra foi de: ")
porcentagem = input("De quantos % é o desconto? ")
# Realizando o calculo
desconto_ = float(valor_da_compra) * float(porcentagem)
# Divisão do calculo em 2 partes
desconto__ = float(desconto_) / 100
# Valor real com desconto aplicado
valor_real = float(valor_da_compra) - float(desconto__)
print("O desconto é de {:.2f} reais".format(desconto__))
print("Portanto o valor a ser pago é de {:.2f} reais" .format(valor_real))