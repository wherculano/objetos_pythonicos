from collections import namedtuple
from random import shuffle
from itertools import product


Carta = namedtuple('Carta', 'valor naipe')


class Baralho:
    valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    naipes = '♦ ♣ ♠ ♥'.split()

    def __init__(self):
        # product faz o conjunto dos valores com os naipes
        # (2, ♦),(2,♣),(2,♠),(2,♥), (3,♦),(3,♣)......
        self.cartas = [Carta(v, n) for n, v in product(self.naipes, self.valores)]

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, posicao):
        return self.cartas[posicao]

    def __setitem__(self, posicao, valor):
        self.cartas[posicao] = valor


if __name__ == '__main__':
    baralho = Baralho()
    for cartas in baralho:
        print(cartas)

    print('-'*20)
    shuffle(baralho)  # embaralhar
    for cartas in baralho:
        print(cartas)