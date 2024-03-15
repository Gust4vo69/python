import random
print('Aluno a apagar o quadro será: ' , random.choice(['gus','lucas','pri']))
names = ['gus', 'lucas', 'prin', 'fernanda', 'paulo']
suffled_names = names.copy()
random.shuffle(suffled_names)
print('A ordem de limpar o quadro é : ', suffled_names)
