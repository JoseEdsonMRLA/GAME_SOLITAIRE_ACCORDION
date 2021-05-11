from random import sample
def cria_baralho():
    baralho=['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']
    indice= sample(range(0,52), 52)
    novo_baralho=[]
    for i in indice:
        carta=baralho[i]
        novo_baralho.append(carta)
    return novo_baralho 

def extrai_naipe(carta):
    naipe=carta[len(carta)-1]
    return naipe

def extrai_valor(carta):
    valor=carta[0:(len(carta)-1)]
    return valor


def lista_movimentos_possiveis(novo_baralho,seleção):
    lista = []
    if seleção == 1:
        return lista
    if extrai_valor(novo_baralho[seleção-1]) == extrai_valor(novo_baralho[seleção-2]) or extrai_naipe(novo_baralho[seleção-1]) == extrai_naipe(novo_baralho[seleção-2]):
        lista.append(1)
    if seleção>3 and seleção<=len(novo_baralho):
        if extrai_valor(novo_baralho[seleção-1]) == extrai_valor(novo_baralho[seleção-4]) or extrai_naipe(novo_baralho[seleção-1]) == extrai_naipe(novo_baralho[seleção-4]):
            lista.append(3)
    else:
        seleção=int(input(f'A carta {novo_baralho[seleção-1]} não pode ser movida. Por favor, digite um número entre 1 e {len(novo_baralho)}: '))
    return lista

def empilha (novo_baralho,seleção, i_d):
    novo_baralho[(seleção-1)-i_d]=novo_baralho[(seleção-1)]
    del novo_baralho[(seleção-1)]
    return novo_baralho

def possui_movimentos_possiveis(novo_baralho):
    for i in range(1,len(novo_baralho)):
        if extrai_valor(novo_baralho[i]) == extrai_valor(novo_baralho[i-1]) or extrai_naipe(novo_baralho[i]) == extrai_naipe(novo_baralho[i-1]):
            return True
        if i>2:
            if extrai_valor(novo_baralho[i]) == extrai_valor(novo_baralho[i-3]) or extrai_naipe(novo_baralho[i]) == extrai_naipe(novo_baralho[i-3]):
                return True
    return False

def pintar(naipe):
    if extrai_naipe(naipe) == '♠':
        blue= '\033[1;36m'
        cor= f'{blue}{naipe}\033[0m'
    if extrai_naipe(naipe) == '♥':
        red= '\033[1;31m'
        cor= f'{red}{naipe}\033[0m'
    if extrai_naipe(naipe) == '♣':
        yellow='\033[1;33m'
        cor= f'{yellow}{naipe}\033[0m'
    if extrai_naipe(naipe) == '♦':
        purple= '\033[1;35m'
        cor= f'{purple}{naipe}\033[0m'
    return cor
print('''
Paciência Acordeão 
================== 

Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 

Existem apenas dois movimentos possíveis: 

1. Empilhar uma carta sobre a carta imediatamente anterior; 
2. Empilhar uma carta sobre a terceira carta anterior. 

Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

1. As duas cartas possuem o mesmo valor ou 
2. As duas cartas possuem o mesmo naipe. 

Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

Aperte [Enter] para iniciar o jogo... 
''')
input()
print('O estado atual do baralho é: ')


novo_baralho = cria_baralho()
while possui_movimentos_possiveis(novo_baralho) == True:
    cont= 1
    for c in novo_baralho:
        # if extrai_naipe(c)=='♦':
        #     carta=f'\033[1;34;40m{naipe}\033[0m'
        # elif extrai_naipe(c)=='♣':
            
        # elif extrai_naipe(c)=='♠':

        # elif extrai_naipe(c)=='♥':

        print(f'{cont}.{pintar(c)}') 
        cont+=1

    seleção = int(input(f'Escolha uma carta (digite um número entre 1 e {len(novo_baralho)}): '))
    while True:
        if seleção <= 0:
            seleção = int(input(f'Escolha uma carta (digite um número entre 1 e {len(novo_baralho)}): '))
        if seleção > len(novo_baralho):
            seleção = int(input(f'Escolha uma carta (digite um número entre 1 e {len(novo_baralho)}): '))
        else:
            break

        
    # while seleção != int() or (seleção <1 and seleção>52) or seleção.isalphabetic()==True :
    #     seleção=input(f'Posição inválida. Por favor, digite um número entre 1 e {len(novo_baralho)}:')        
        
    
    if len(lista_movimentos_possiveis(novo_baralho,seleção))== 0:
        while len(lista_movimentos_possiveis(novo_baralho,seleção)) == 0:
            seleção= int(input(f'A carta {novo_baralho[seleção-1]} não pode ser movida. Por favor, digite um número entre 1 e {len(novo_baralho)}: '))
            if len(lista_movimentos_possiveis(novo_baralho,seleção)) > 0:
                while True:
                    if seleção <= 0:
                        seleção = int(input(f'Escolha uma carta (digite um número entre 1 e {len(novo_baralho)}): '))
                    if seleção > len(novo_baralho):
                        seleção = int(input(f'Escolha uma carta (digite um número entre 1 e {len(novo_baralho)}): '))
                    else:
                        break
            else:
                continue
            # break

    elif len(lista_movimentos_possiveis(novo_baralho,seleção)) == 1:
        if lista_movimentos_possiveis(novo_baralho,seleção)[0] == 1:
            i_d= 1
        if lista_movimentos_possiveis(novo_baralho,seleção)[0] == 3:
            i_d= 3
        novo_baralho=empilha(novo_baralho,seleção,i_d)
            
                
    elif len(lista_movimentos_possiveis(novo_baralho,seleção)) == 2:
        print(f'Sobre qual carta você deseja empilhar o {novo_baralho[seleção-1]}?')
        print(f'1.{novo_baralho[seleção-1-1]}')
        print(f'2.{novo_baralho[seleção-1-3]}')
        decisão=int(input(f'Digite o número de sua escolha (1-{len(novo_baralho)}): '))
        while decisão!=1 and decisão!=2:
            print(f'Opção inválida. Sobre qual carta você quer empilhar o {novo_baralho[seleção-1]}?') 
            print(f'1.{novo_baralho[seleção-1-1]}')
            print(f'2.{novo_baralho[seleção-1-3]}')
            decisão=int(input(f'Digite o número de sua escolha (1-{len(novo_baralho)}): '))
        if decisão == 1:
            i_d= 1
            novo_baralho=empilha(novo_baralho,seleção,i_d)
        elif decisão==2:
            i_d=3
            novo_baralho=empilha(novo_baralho,seleção,i_d)
        
    elif possui_movimentos_possiveis(novo_baralho) == False:
        if len(novo_baralho)==1:
            print('Você venceu! :)')
            
        if len(novo_baralho)>1:
            print('Você perdeu! :(')

        vontade=input('Você quer jogar novamente (digite sim ou não)? ')
        if vontade== 'sim': 
            possui_movimentos_possiveis(novo_baralho) == True
        else:
            break