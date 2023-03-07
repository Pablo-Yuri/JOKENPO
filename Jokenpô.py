from random import choice
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
azul2 = '\033[1;36m'
limpo = '\033[m'
print('{}'.format(amarelo),'= '*12,'\n'
      '{}  Vamos jogar Jokenpô!'.format(azul2),'\n',
      '{}= '.format(amarelo)*12)
print('{}Pedra, Papel ou Tesoura?'.format(roxo))
pc = choice(['PEDRA','PAPEL','TESOURA'])
jogador = input('{}Escolha: '.format(verde)).upper().strip()
if jogador == pc:
    print('{}EMPATE!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul,amarelo, pc,azul,amarelo, jogador,azul))
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print('{}VOCÊ GANHOU!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul, amarelo, pc, azul, amarelo, jogador, azul))
elif jogador == 'TESOURA' and pc == 'PEDRA':
    print('{}VOCÊ PERDEU!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul, amarelo, pc, azul, amarelo, jogador, azul))
elif jogador == 'PAPEL' and pc == 'TESOURA':
    print('{}VOCÊ PERDEU!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul, amarelo, pc, azul, amarelo, jogador, azul))
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print('{}VOCÊ GANHOU!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul, amarelo, pc, azul, amarelo, jogador, azul))
elif jogador == 'PEDRA' and pc == 'PAPEL':
    print('{}VOCÊ PERDEU!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul, amarelo, pc, azul, amarelo, jogador, azul))
elif jogador == 'PEDRA' and pc == 'TESOURA':
    print('{}VOCÊ GANHOU!!'.format(vermelho))
    print('{}O computador jogou {}{}{} e você jogou {}{}{}!!'.format(azul, amarelo, pc, azul, amarelo, jogador, azul))
