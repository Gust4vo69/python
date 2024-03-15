frase =  'Olá, você esta bem?'
print(frase.find('o'))#retorna a posição da letra minuscula o na string
print(len(frase))#retorna o tamanho da string
print(frase[0:4])#mostra os caracteres do indice 0 até o 3 (não inclui o 4)
print(frase[:4]) #mesma coisa
print("Estou" in frase)#verifica se existe a palavra "estou" na string
print(frase.find('estou'))#retorna a posição da primeira ocorrência de "estou", se não existir retorna -1
palavras = frase.split()#divide a string em uma lista de strings separadas por espaços em branco
print(palavras)

dividido = frase.split(' ') #utiliza um caractere para dividir a string
print(frase.split())#sem argumento split(), ele divide a string em uma lista de strings usando os espacos em branco
print(dividido)

print(frase.upper( ))#converte todos os caracteres da string para maiúsculas
print(frase.lower( ))#converte todos os caracteres da string para minúsculas
print(frase.capitalize())#coloca a primeira letra de cada palavra maiuscula
frase2 = '  ola tudo bem?   '
print(frase2.strip())#remove os espacos em branco no começo e no fim da string
print("-"*5)
print("""Salve, tudo bem
qual seu nome?
sua idade e moradia""")
print("-"*5)
print(frase.replace( 'bem', 'mal' ))#troca todas as ocorrencias de 'bem' por 'mal'
maiuscula = 'OLA, ESSA É UMA FRASE MAIUSCULA'
print(maiuscula)
print(maiuscula.isupper())#retorna True se toda a string estiver em Maiusculo
print(maiuscula.lower( ))#transforma em minusculas
print(maiuscula.istitle())#retorna True se toda a string estiver em titulo (primeira letra de cada palavra maiuscula)
print(frase.title())#deixa a primeira letra de cada palavra maiuscula
print(frase.len(frase))#retorna o numero total de letras na string