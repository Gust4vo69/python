print('calculo de aumento de salario')
salario = float(input('Qual o salario que deseja aumentar?\n'))
porcem = float(input('Quer aumentar em quantos %?\n'))
porcemf = porcem/100
aumento = (porcemf*salario)
salarionovo = salario + aumento


print('Dando {} porcento de aumento em cima do salario de {}, tera um aumento de {} reais e o total será: {} reais.' .format(porcem, salario, aumento, salarionovo ))