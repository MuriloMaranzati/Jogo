import random


print('1 = Pedra')
print('2 = papel')
print('3 = tsoura')

c = 0
while c < 3:
    escolha = int(input('Qual opção vc quer: '))
    pedra = 1
    papel = 2
    tesoura = 3
    robo = random.randint(1,4)

    print(f'robô {robo}')

    if escolha == robo:
        print('empate')
    elif escolha == 1 and robo == 2:
        print('perdeu')
    elif escolha == 1 and robo == 3:
        print('ganhou')
    c += 1
