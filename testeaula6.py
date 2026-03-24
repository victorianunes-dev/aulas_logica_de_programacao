nome = str(input("Digite seu nome:"))
rua = str(input("Seu endereço:"))
telefone = int(input("Seu telefone:"))

print("Olá, {}".format(nome))
print("Dados salvos com sucesso!")
print("Entraremos em contato pelo numero {} para confirmar o agendamento".format(telefone))