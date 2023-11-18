from random import randint
itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
computador = randint(0, 4)
jogador= int(input('Escolha entre: 0 - Pedra, 1 - Papel, 2 - Tesoura, 3 - Lagarto e 4 - Spock: '))
print('-=' * 11)
print ('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0: #computador jogou Pedra
 if jogador == 0:
  print ("Empate")
 elif jogador == 1:
  print ('Papel cobre Pedra, jogador vence')
 elif jogador == 2:
  print ('Pedra esmaga Tesoura, computador vence')
 elif jogador == 3:
  print ('Pedra esmaga Lagarto, computador vence')
 elif jogador == 4:
  print ('Spock vaporiza Pedra, jogador vence')
  
elif computador == 1:
 if jogador == 0:
  print ('Papel cobre Pedra, computador vence')
 elif jogador == 1:
  print('Empate')
 elif jogador == 2:
  print ('Tesoura corta Papel, jogador vence')
 elif jogador == 3:
  print('Lagarto come o Papel, jogador vence')
 elif jogador == 4:
  print ('Papel refuta spock, computador vence')

elif computador == 2:
 if jogador == 0:
  print('Pedra esmaga Tesoura, jogador vence')
 elif jogador == 1:
  print('Tesoura corta Papel, computador vence')
 elif jogador == 2:
  print('Empate')
 elif jogador == 3:
  print('Tesoura decapita Lagarto, computador vence')
 elif jogador == 4:
  print('Spock destroi Tesoura, jogador vence')

elif computador == 3:
 if jogador == 0:
  print('Pedra esmaga Lagarto, jogador vence')
 elif jogador == 1:
  print('Lagarto come Papel, computador vence')
 elif jogador == 2:
  print('Tesoura decapita Lagarto, jogador vence')
 elif jogador == 3:
  print('Empate')
 elif jogador == 4:
  print('Lagarto envenena Spock, computador vence')

elif computador == 4:
 if jogador == 0:
  print('Spock vaporiza Pedra, computador vence')
 elif jogador == 1:
  print('Papel refuta spock, jogador vence')
 elif jogador == 2:
  print('Spock destroi Tesoura, computador vence')
 elif jogador == 3:
  print('Lagarto envenena Spock, jogador vence')
 elif jogador == 4:
  print('Empate')