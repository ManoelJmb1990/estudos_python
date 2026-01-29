len("123456")
# TypeError: object of type 'int' has no len()
# acima é um exemplo de TypeError, que ocorre quando uma operação ou função é 
# aplicada a um objeto de um tipo inadequado.

# Demonstra o uso da função type() para identificar os tipos de dados:
# inteiro (int), ponto flutuante (float), booleano (bool) e NoneType
print(type(123456))
print(type(1.5))
print(type(True))
print(type(False))
print(type(None))
