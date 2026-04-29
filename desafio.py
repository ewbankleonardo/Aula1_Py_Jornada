#Digite o nome

nome = input("Digite seu nome: ")

#Salario

sal=float(input("Digite o seu salário: "))

#Bonus

bon=float(input("Digite o valor do bonus: "))

#calculo KPI
kpi = 1000 + sal*bon

print(f"Ola,{nome}, o valor de seu bônus foi de {kpi} ")