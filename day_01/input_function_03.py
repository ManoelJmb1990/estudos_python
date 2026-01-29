print("Sem variável")
input("What is your name? ")
# O input acima solicita ao usuário que insira seu nome, mas não armazena o valor inserido em nenhuma variável.
# Para armazenar o valor inserido, devemos atribuí-lo a uma variável.


print("\nCom variável")
name = input("What is your name? ")
print(name)
# No código acima, o valor inserido pelo usuário é armazenado na variável 'name' e depois impresso na tela.

print("\nConcatenação")
print("Hello " + input("What is your name? ") + "!")
# No código acima, o valor inserido pelo usuário é diretamente concatenado com 
# a string "Hello " e "!" para formar uma saudação completa.

