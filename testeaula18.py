def calcular_ir_2026(salario):
    # Desconto simplificado padrão
    desconto_simplificado = 607.20
    
    # Base de cálculo
    base = salario - desconto_simplificado

    if base <= 0:
        return 0

    # Tabela progressiva
    if base <= 2428.80:
        imposto = 0
    elif base <= 2826.65:
        imposto = (base * 0.075) - 182.16
    elif base <= 3751.05:
        imposto = (base * 0.15) - 394.16
    elif base <= 4664.68:
        imposto = (base * 0.225) - 675.49
    else:
        imposto = (base * 0.275) - 908.73

    # 🔻 Regra nova de redução 2026
    if salario <= 5000:
        reducao = min(imposto, 312.89)
        imposto -= reducao
    elif salario <= 7350:
        reducao = 978.62 - (0.133145 * salario)
        reducao = max(0, reducao)
        imposto -= min(imposto, reducao)

    # Imposto nunca negativo
    return max(imposto, 0)


# Programa principal
salario = float(input("Digite seu salário mensal: R$ "))

ir = calcular_ir_2026(salario)

print(f"Salário: R$ {salario:.2f}")
print(f"Imposto de Renda devido: R$ {ir:.2f}")