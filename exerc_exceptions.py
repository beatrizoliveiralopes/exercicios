
nome = input("Digite o seu nome completo: ")
ano = input("Digite o ano de seu nascimento: ")
print("     " ,nome, "    ",ano)

try:
        if int(ano) >1922 & int(ano)<=2021:
              print(" Vc completou/completará ", 2023 - int(ano) , "anos")
        else:
              print("Data Invalida")
except:
        print("Vc deve digitar valores válidos")
