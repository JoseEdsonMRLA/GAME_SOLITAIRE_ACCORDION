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


def lista_movimentos_possiveis(baralho,i):
    lista = []
    if i == 0:
        return lista
    if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]):
        lista.append(1)
    if i>2:
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]):
            lista.append(3)
    return lista

def empilha (baralho, i_o, i_d):
    baralho[i_d]=baralho[i_o]
    del baralho[i_o]
    return baralho


def possui_movimentos_possiveis(baralho):
    for i in range(1,len(baralho)):
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]):
            return True
        if i>2:
            if extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]):
                return True
    return False
      
