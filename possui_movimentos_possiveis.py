def extrai_valor(carta):
    valor=carta[0:(len(carta)-1)]
    return valor
def extrai_naipe(carta):
    return carta[len(carta)-1]
def possui_movimentos_possiveis(baralho):
    for i in range(1,len(baralho)):
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]):
            return True
        if i>2:
            if extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]):
                return True
    return False
      