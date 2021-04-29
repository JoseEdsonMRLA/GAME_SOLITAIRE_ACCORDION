def extrai_valor(carta):
    valor=carta[0:(len(carta)-1)]
    return valor
def extrai_naipe(carta):
    return carta[len(carta)-1]
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