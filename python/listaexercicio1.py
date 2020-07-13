# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def alo_mundo():
    print("Alô, mundo!!")


# Faça um Programa que peça um número e então mostre a 
# mensagem O número informado foi [número].
def mostra_numero():
    numero = int(input("Informe um número: "))
    print(f"O número informado foi: {numero}.")

# Faça um Programa que peça dois números e imprima a soma.
def soma():
    try:
        numero1 = int(input("Informe um número: "))
        numero2 = int(input("Informe outro número: "))
        resultado = numero1 + numero2
        print(f"A soma dos número informado é {resultado}.")
        
    except:
        print("Erro! O valor informado deve ser um número inteiro.")


# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def medias():
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"A média das notas é {media}.")

# Modo pythônico
def media_pythonic():
    notas = [float(input("Insira a nota: ")) for i in range(4)]
    media = sum(notas)/len(notas)
    print(f"A média é {media}.")


# Faça um Programa que converta metros para centímetros.
def m_cm(valor: float):
    cm = valor * 100
    print(f"{valor}m (metros) equivale a {cm}cm (centímetro).")


# Faça um Programa que peça o raio de um círculo, 
# calcule e mostre sua área.
def area_circulo(raio: int):
    pi = 3.14
    A = pi*(raio**2)
    print("A área do círculo informado é {}".forma(A))


# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.
def area_quadrado(base: int):
    area = base**2
    print(f"A aréa do quadro de base {base} é: {area}.")
    print(f"O dobro da area é: {2*area}")


# Faça um Programa que pergunte quanto você 
# ganha por hora e o número de horas trabalhadas 
# no mês. Calcule e mostre o total do seu salário no referido mês.
def salario():
    valor_hora_trab = float(input("Informe o valor da sua hora de trabalho: "))
    horas_trab = int(input("Informe a quantida de horas mensais trabalhadas: "))
    salario_mensal = horas_trab * valor_hora_trab
    print("Seu salário mensal é R$ {salario_mensal}.")


# Faça um Programa que peça a temperatura em graus Farenheit, 
# transforme e mostre a temperatura em graus Celsius. 
# C = (5 * (F-32) / 9). 
def Far_cel(faren: float):
    celsius = (5*(faren-32)/9)
    print(f"A temperatura em graus Celsius é {celsius}º.")


Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. 

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 