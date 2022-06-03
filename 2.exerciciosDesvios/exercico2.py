conta = int(input("Digite os 3 digitos de sua conta: ")) #235
if conta>999 or conta<0:
   print("erro, digite apenas três digitos")
else:
    digito1 = conta % 10 #digito1 = 235 % 10 qual é o resto?  = digito1 = 5
    digito2 = (conta//10) %10 #digito2 = 235 // 10 eu quero o quociente. 23%10 eu quero o resto = digito2 = 3
    digito3 = (conta//100)  #digito3 = 235 // 100 = 2
    digito1_inverso = digito1 *100 #5 * 100 = 500
    digito2_inverso = digito2 *10 #3 * 10 = 30
    inverso = digito1_inverso + digito3 + digito2_inverso #500 + 2 + 30  = 532
    juncao = conta + inverso # 767
    juncao1 = juncao %10
    juncao2 = (juncao//10) %10
    juncao3 = (juncao//100)
    verificador = juncao1 + (juncao2 *2) + (juncao3*3)
    digito_verificador = verificador % 10
    print("O número ", conta, " + ", inverso, " é igual à", juncao)
    print("A multiplicação pela ordem posicionaal ficaria: ", juncao1, "x 1 +",juncao2, "x 2 +", juncao3, "x 3 =", verificador )
    print("E o digito verificador seria: ", digito_verificador)