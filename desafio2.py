#Identificar possíveis possibilidades de erro nesse código(try-excepet, if-else-elif):

#nome = 33 é um erro? (digitou numeros ou deixou em branco )
nome = input("Digite seu nome: ")

if nome.isdigit():
    print("Usuário inválido!")
    exit()
elif len(nome) == 0:
    print("Você não digitou seu nome")
    exit()
elif nome.isspace():
    print("Voce digitou só espaço")
    exit()
else:
    pass

#Adicionar número negativo ou nao digitar
try :
    salario = float(input("Digite seu salario: "))

    if salario < 0:
        print("Insira um numero positivo")
        exit()
    
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# O usuario pode tentar escrever por extenso:
try:
    porcentagem_do_bonus = float(input("porcentagem do bonus em %: "))

except ValueError:
    print("Apenas números, por favor!")
    exit()

valor_do_bonus = 1000 + (salario) * (porcentagem_do_bonus) / 100 

print(f"O usuario {nome} possui bonus de {valor_do_bonus}")

salario_total = float(salario) + valor_do_bonus

print(f"O salario total do usuario {nome} é de {salario_total}")

