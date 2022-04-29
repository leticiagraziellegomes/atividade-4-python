nome = input("Digite seu primeiro nome: ")

primeiraLetra = nome[0:1].upper()
restantenome = nome[1:10].lower()

nome = primeiraLetra + restantenome

dia = input("Dia do nascimento: ")
mes = input("Mes do nascimento: ")
ano = input("Ano do nascimento: ")


print("{} nasceu no dia: {}/{}/{}" .format(nome,dia,mes,ano))




