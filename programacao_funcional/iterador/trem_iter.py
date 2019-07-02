# Implementando Trem com o iterador __iter__
class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __iter__(self):
        return IteradorTrem(self.num_vagoes)


class IteradorTrem:
    def __init__(self, num_vagoes):
        self.atual = 0
        self.ultimo_vagao = num_vagoes - 1

    # responsavel pela iteracao nos elementos dentro do laço for
    def __next__(self):
        if self.atual <= self.ultimo_vagao:
            self.atual += 1
            return f'Vagão #{self.atual}'
        else:
            raise StopIteration  # para de iterar sobre o elemento após o ultimo valor


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
