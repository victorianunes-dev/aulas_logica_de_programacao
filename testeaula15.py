capacidade = float(input("Digite a capacidade máxima do elevador (kg): "))

p1 = float(input("Digite o peso da 1ª pessoa: "))
p2 = float(input("Digite o peso da 2ª pessoa: "))
p3 = float(input("Digite o peso da 3ª pessoa: "))
p4 = float(input("Digite o peso da 4ª pessoa: "))
p5 = float(input("Digite o peso da 5ª pessoa: "))

total = p1 + p2 + p3 + p4 + p5

if total <= capacidade:
    print("Elevador liberado para subir.")
else:
    print("Carga máxima excedida!")