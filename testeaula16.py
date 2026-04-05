print("Escolha o tipo de objeto: ")
print("1 - Lata de óleo")
print("2 - Caixa de papelão")

opcao = int(input("Digite a opção (1 ou 2): "))

if opcao == 1:
    raio = float(input("Digite o raio da lata em cm: "))
    altura = float(input("Digite a altura da lata em cm: "))
    
    volume = 3.14159*raio**2*altura

    print("Volume da lata de óleo: ", volume)

else:
    if opcao == 2:
        altura = float(input("Digite a altura da caixa em cm: "))
        largura = float(input("Digite a largura da caixa em cm: "))
        comprimento = float(input("Digite o comprimento da caixa em cm: "))

        volume = altura*largura*comprimento

        print("Volume da caixa de papelão: ", volume)

    else:
         print("Opção inválida!")