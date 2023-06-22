# 1- Faça um Programa que mostre a mensagem "Alo mundo" na tela.
import math
print('Alo mundo!')


# 2- Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
n1 = int(input('Digite um número: '))
print('O numero informado foi', n1)


# 3- Faça um Programa que peça dois números e imprima a soma.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
print(soma)


# 4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = int(input('Digite a 1º nota bimestral: '))
n2 = int(input('Digite a 2º nota bimestral: '))
n3 = int(input('Digite a 3º nota bimestral: '))
n4 = int(input('Digite a 4º nota bimestral: '))
media = (n1+n2+n3+n4)/4
print(media)


# 5- Faça um Programa que converta metros para centímetros.
metros = float(input('Digite um número: '))
cent = (metros)*100
print(int('Este Número em centimetros sera:{}'.format(cent)))


# 6- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input('Digite o raio de um circulo: '))
area = math.pi*raio**2
print(area)


# 7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
num = int(input('Digite o número: '))
area = num**2
area *= 2
print(area)
print()


# 8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hr = float(input('Digite quanto você recebe por hora trabalhada: '))
hora = float(input('Digite o número de horas trabalhadas: '))
hora *= 60
min = float(input('Digite os minutos restantes:'))
valor_total = (((hora+min)*valor_hr)/60)
print('O valor total do salario é:{}'.format(valor_total))


# 9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
graus_Fahrenheit = float(input('Digite os graus_Fahrenheit'))
conv = (graus_Fahrenheit-32)*1.8
print(conv)


# 10- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input('Digite os graus_celsius'))
graus_Fahrenheit = (celsius*1.8)+32
print(graus_Fahrenheit)

# 11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero interiro: '))
real = float(input('Digite um numero real: '))
print(num1)
print(num2)
print(real)
calc1 = (num1*2)*(num2/2)
print(calc1)
calc2 = (num1*3)+(real)
print(calc2)
calc3 = real**3
print(calc3)


# 12- Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.1
altura = float(input('Digite a altura da pessoa: '))
pes_ideal = (72.7 * altura) - 58.1
print(pes_ideal)


# 13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input('Digite a altura da pessoa: '))
pes_ideal = (72.7 * altura) - 58.1
print(pes_ideal)


# 14-  João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#  deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#  e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
#  que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


# 15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
val_hora = float(input("Digite o quanto você ganha por hora: "))
num_horas = float(input("Digite o número de horas trabalhadas no mês: "))
# a)Salário bruto.
total_sal = val_hora * num_horas
print('O valor total do salario é !: {}'.format(total_sal))
# b)Quanto pagou ao INSS.
pag_inss = total_sal*0.08
print('O valor total pago ao inss é !: {}'.format(pag_inss))
# c)Quanto pagou ao sindicato.
pag_sind = total_sal*0.05
print('O valor total pago ao sindicato é !: {}'.format(pag_sind))
# d)O salário líquido.
sal_liq = total_sal - pag_inss - pag_sind
resultado = (f'{sal_liq:.2f}')
print('O valor so salario liquido equivale a: {} '.format(resultado))


# 16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = float(input('Informe o tamanho da área a ser pintada em m^2: '))
tinta_necessaria = area/3
latas_resto = (tinta_necessaria//18)
latas = (tinta_necessaria/18)
preco_total = latas*80
if latas_resto > 0:
    latas += 1
    resultado = int(latas)
    resultado2 = (f'{preco_total:.2f}')
    print('latas necessárias: {}'.format(resultado))
    print('Valor total a pagar: {}'.format(resultado2))
else:
    print('latas necessárias: {}'.format(latas))
    print('Valor total a pagar: R${}'.format(resultado2))
