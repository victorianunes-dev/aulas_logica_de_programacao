salario = float(input("Digite o valor do salário: "))
reajuste = float(input("Porcentagem de reajuste (%): "))

valor = (salario/100*reajuste ) + salario

print("Seu novo salário reajustado:", valor)