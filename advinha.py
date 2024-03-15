import random
print('Vamos começar o jogo da advinhação!')
num = random.randint(0, 5)
n = int(input('Pensei em um numero de 1 a 5, tente adivinhar:\n'))
if n == num:
    print('Você Acertou! Parabéns!')
else:
    print('Hum, que pena, você errou.')
    choice = input('Quer tentar novamente? [S/N]').upper()
    if choice == 'S':
        while True:
            n = int(input('Tente outro número:\n'))
            if n == num:
                print('Acertou também dessa vez! Parabéns!')
                break
            else:
                print('Errou ainda...')

