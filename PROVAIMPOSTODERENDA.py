# base de calculo
salariobruto = float(input("Digite o seu salário bruto: "))

# desconto fixo de inss

descontofixo = 607.20
basedecalculo = salariobruto - descontofixo
valorminimo = 5000

# Tabela progressiva

if salariobruto <= 5000:
    imposto = 0
elif salariobruto > 5000:
    if basedecalculo <= 2428.80:
        imposto = 0
    elif basedecalculo <= 2826.65:
        imposto = (basedecalculo * 0.075) - 182.16
    elif basedecalculo <= 3751.05:
        imposto = (basedecalculo * 0.15) - 394.16
    elif basedecalculo <= 4664.68:
        imposto = (basedecalculo * 0.225) - 675.49
    elif basedecalculo > 4665.68:
        imposto = (basedecalculo * 0.275) - 908.73

# Regra de redução 2026

if salariobruto <= 5000:
    reducao = 0
elif salariobruto <= 7350:
    reducao = 978.62 - (0.133145 * salariobruto)
elif salariobruto > 7350:
    reducao = 0

# Calculando o imposto

impostoreal = imposto - reducao
salarioreal = basedecalculo - impostoreal
descontototal = impostoreal

# resultados

if descontototal > descontofixo:
    print("O valor de desconto no seu salario (IMPOSTO DE RENDA) foi de: R$", descontototal)
    print("O valor liquido do seu salario é de: R$", salarioreal)

if descontototal <= descontofixo:
    print("Você nao tem imposto de renda a descontar.")
    print("O valor liquido do seu salario é de: R$", salariobruto)

elif basedecalculo < 2428.80:
    print("Seu salário não teve descontos de aliquotas.")
elif basedecalculo <= 2826.65:
    print("Seu salário entrou na aliquota de 7,5%.")
elif basedecalculo <= 3751.05:
    print("Seu salário entrou na aliquota de 15%.")
elif basedecalculo <= 4664.68:
    print("Seu salário entrou na aliquota de 22,5%.")
elif basedecalculo > 4665.68:
    print("Seu salário entrou na aliquota de 27,5%.")
