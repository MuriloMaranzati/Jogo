import random
import emoji


print(emoji.emojize('Pedra :black_circle:'))
print(emoji.emojize('Papel :roll_of_paper:'))
print(emoji.emojize('Tesoura :scissors:'))
print(emoji.emojize('Sair :END_arrow:'))

while True:
    escolha = str(input('\nQual opção vc quer: '))

    opcao = ['Pedra', 'Papel', 'Tesoura']
    robo = random.choice(opcao)

    if escolha == 'Sair':
        break

    if robo == 'Pedra':
        print(emoji.emojize('ROBÔ: Pedra :black_circle:'))
    elif robo == 'Papel':
        print(emoji.emojize('ROBÔ: Papel :roll_of_paper:'))    
    elif robo == 'Tesoura':
        print(emoji.emojize('ROBÔ: Tesoura :scissors:'))

    if escolha == robo:
        print('\033[1mEMPATE\033[m')
    elif escolha == 'Pedra' and robo == 'Papel':
        print('\033[1;31mPERDEU\033[m')
    elif escolha == 'Papel' and robo == 'Tesoura':
        print('\033[1;31mPERDEU\033[m')
    elif escolha == 'Tesoura' and robo == 'Pedra':
        print('\033[1;31mPERDEU\033[m')
    elif escolha == 'Pedra' and robo == 'Tesoura':
        print('\033[1;32mGANHOU\033[m')
    elif escolha == 'Papel' and robo == 'Pedra':
        print('\033[1;32mGANHOU\033[m')
    elif escolha == 'Tesoura' and robo == 'Papel':
        print('\033[1;32mGANHOU\033[m')
  