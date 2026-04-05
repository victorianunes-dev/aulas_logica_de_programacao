print("Escolha o tipo de forma: ")
print("1 - Retângulo")
print("2 - Triângulo")

opcao = int(input("Digite a opção (1 ou 2): "))

if opcao == 1:
    base = float(input("Digite a base do retângulo em cm: "))
    altura = float(input("Digite a altura do retângulo em cm: "))
    
    area = base*altura

    print("Area total do retângulo (cm): ", area)

else:
    if opcao == 2:
        base = float(input("Digite a base do triângulo em cm: "))
        altura = float(input("Digite a altura do triângulo em cm: "))
    
        area = (base*altura)/2

print("Area total do triângulo (cm): ", area)

