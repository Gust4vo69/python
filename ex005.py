print('Calculo de aluguel de veiculo alugado')
dias = float(input('Informe quantos dias o carro foi utilizado:\n'))
km = float(input('Informe quantos quilometros foram rodados:\n'))
cdias = dias * 60
ckm = km * 0.15
total = cdias + ckm
print('Foi rodado {} quilometros em {} dias, o total a se pagar é: R${}'.format(km, dias, total))

