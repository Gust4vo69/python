print('Seja bem vindo ao radar de velocidade')
vel = int(input('Digite a velocidade que foi registrada no radar:\n'))
velp  = 80
if vel > velp:
    multa = (vel - velp) * 7 
    print('O veiculo passou da velocidade permitida e será multado em {} reais' .format(multa))
else:
    print('Velocidade dentro do Limite da via')
    

    