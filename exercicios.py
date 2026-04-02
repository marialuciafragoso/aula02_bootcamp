# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#?try:
    #?numero_1 = int(input("Digite o primeiro número inteiro: "))
    #?numero_2 = int(input("Digite o segundo número inteiro: "))
    #?print (f"A soma de {numero_1} e {numero_2} é igual a {numero_1 + numero_2}")
#except:
    #?print("Insira um número inteiro")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#?try:
    #?num_usuario = int(input("Digite um número inteiro: "))
    #?resto_divisao = num_usuario % 5
    #?print(f"O resto da divisão do número {num_usuario} por 5 é {resto_divisao}")
#?except:
    #?print("Insira um número inteiro")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#?try:
    #?num_1 = int(input("Digite um número: "))
    #?num_2 = int(input("Digite outro número: "))
    #?multiplicaçao = num_1 * num_2
    #?print(f"O resultado da multiplicação é {multiplicaçao}")
#?except:
    #?print("Insira um número inteiro")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#?try:
    #?numero_1 = int(input( "Digite um numero inteiro:"))
    #?numero_2 = int(input("Digite outro numero inteiro:"))
    #?divisao_inteira = numero_1 // numero_2
    #?print(f"A divisão de {numero_1} por {numero_2} é igual a {divisao_inteira}")
#?except:
    #?print("Não é possível realizar essa operação!")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#?try:
    #?numero = int(input("Digite um numero: "))
    #?numero_quadrado = numero ** 2
    #?print(f"O número {numero} ao quadrado é {numero_quadrado}")
#?except:
    #?print("Insira um número inteiro")

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
try:
    numero_1 = float((input("Digite o primeiro número: ")).replace(",","."))
    numero_2 = float((input("Digite o segundo número: ")).replace(",","."))
    print (f"A soma de {numero_1} e {numero_2} é igual a {numero_1 + numero_2}")
except:
    print("Insira um número!")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print("Cálculo da media de dois numeros!")
numero_1 = float((input("Digite o primeiro número: ")).replace(",","."))
numero_2 = float((input("Digite o segundo número: ")).replace(",","."))
media = (numero_1 * numero_2) / 2
print(f"A media é: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math


raio_do_circulo = float(input("Digite o raio do círculo: "))
area_circulo = math.pi * raio_do_circulo**2
print(f"{area_circulo: .2f}")
print(f"a área do círculo é igual a {area_circulo: .2f}")

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data = str(input("Digite uma data no modelo dd/mm/aaaa: "))
#dia, mes, ano = data.split("/")
#print(f"Dia é {dia}")
#print (f"Mês é {mes}")
#print (f"Ano é {ano}")



# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação