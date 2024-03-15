name = input('Write the name of the studant:\n')
n1 = float(input('Write the first grade:\n'))
n2 = float(input('Write the second grade:\n'))
media = (n1+n2)/2
print('The average of {} is {:.1f}.' .format(name, media))