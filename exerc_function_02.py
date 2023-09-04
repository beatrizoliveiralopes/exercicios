print("CALCULADORA ")
print("\n 1. ADIÇÃO \n 2.SUBTRAÇÃO \n 3.MULTIPLICAÇÃO \n 4.DIVISÃO \n 0. SAIR")
opcao = input("Digite a opção desejada: ")

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
def calculadora (num1, num2, opcao):
    if opcao == '1':
       resultado = num1 + num2
       return resultado
    elif opcao == '2':
        resultado = num1 - num2
        return resultado
    elif opcao == '3':
        resultado = num1 * num2
        return resultado
    elif opcao == '4':
        resultado = num1 / num2
        return int(resultado)
    elif opcao == '0':
        print("SAINDO...")

resultado = calculadora(int(num1), int(num2), opcao)
print(resultado)