print("Seja bem-vindo ao programa de calculo do valor da passagem de onibus")
km = float(input("Digite quantos quilometros  serão percorridos: "))
if km <= 200:
    preço = km * 0.50
    print('O valor da sua passagem será {} reais'.format(preço))
else:
    preço = km * 0.45
    print('O valor da sua passagem será de {} reais.'.format(preço))
