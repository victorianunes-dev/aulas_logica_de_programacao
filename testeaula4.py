nome = str(input("Informe seu nome: "))
nasc = int(input("Informe ano de nascimento: "))
hoje = int(input("Informe ano atual: "))
idade = hoje-nasc
print("Olá, {}".format(nome))
print("você possui em torno de {} anos de idade".format(idade))
