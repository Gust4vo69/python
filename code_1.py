name = input('tell me your name: ')
age = input('how old are you? ')

print("Your wellcome " + name + ", you are " + age + " years old, right?", end=" --- ")
print("Seja bem vindo {0}, voce tem {1} anos , correto?".format( name, age))
n1 = int(input('Give me a number:\n'))
n2 = int(input('Give me another number:\n'))
tchoice = input('Send A to + and B to -\n')

if(tchoice == "A" or tchoice == "a"):
    sum = n1 + n2 
    print('A soma é:\n',sum)
else:
    if (tchoice == "B" or tchoice == "b"):
        sub = n1 - n2
        print('A subtração é:\n', sub)
    else: 
        print("operação invalida")   
    
