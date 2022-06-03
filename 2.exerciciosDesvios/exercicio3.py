numero_1 = 15
numero_2 = 6
resultado = ((numero_1 % 2) * 3) + (13 - 2 + numero_2)
# resultado = ((15%2)*3)+(13-2+6)
# resultado = (1 * 3) + (13 - 2 + 6)
# resultado = 3 + 17
# resultado = 20
print(resultado)

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
resultado = ((numero1 % 2) * 3) + (13 - 2 + numero2)
# resultado<- ((numero_1 mod 2) * 3) + (13 - 2 + numero_2)

if (resultado <= 0):
    print("resultado menor ou iguala zero")
else:
    # if((resultado>0) and (resultado<=20)):
    if resultado <= 20:
        print("resultado maior que zero e menor ou igual a 20")
    else:
        print("Resultado maior que 20")
print(resultado)
