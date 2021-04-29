def empilha (baralho, i_o, i_d):
    baralho[i_d]=baralho[i_o]
    del baralho[i_o]
    return baralho
    