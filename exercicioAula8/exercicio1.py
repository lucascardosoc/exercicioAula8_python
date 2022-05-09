destino = int(input('-Selecione seu destino-'
                '\n1.Norte'
                '\n2.Nordeste'
                '\n3.Centro-Oeste'
                '\n--> '))
if destino in [1,2,3]:
    if destino == 1:
        destinoSelecionado = 'Norte'
    elif destino == 2:
        destinoSelecionado = 'Nordeste'
    else:
        destinoSelecionado = 'Centro-Oeste'

    passagens = int(input('Passagem de ida e volta? '
                      '\n1.SIM'
                      '\n2.NÃO'
                      '\n--> '))
    if passagens == 1 or passagens == 2:
        if destinoSelecionado == 'Norte' and passagens == 1:
            precoFinal = 400
        elif destinoSelecionado == 'Norte' and passagens == 2:
            precoFinal = 280
        elif destinoSelecionado == 'Nordeste' and passagens == 1:
            precoFinal = 628
        elif destinoSelecionado == 'Nordeste' and passagens == 2:
            precoFinal = 380
        elif destinoSelecionado == 'Centro-Oeste' and passagens == 1:
            precoFinal = 1100
        else:
            precoFinal = 620
        print(f'Sua viagem para {destinoSelecionado} tem o valor de {precoFinal} Reais')
    else:
        print("Você escolheu um número diferente de 1 e 2")