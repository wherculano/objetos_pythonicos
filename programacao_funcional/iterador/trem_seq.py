class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, posicao):
        indice = posicao if posicao >= 0 else self.num_vagoes + posicao
        if 0 <= indice < self.num_vagoes: # se  o indice for igual a 2 por exemplo, retornará o vagao 3
            return f'Vagao #{indice+1}'
        else:
            raise IndexError(f'Vagão #{posicao} inexistente!')


if __name__ == '__main__':
    trem = Trem(4)
    for vagao in trem:
        print(vagao)

    print(f'Tamanho: {len(trem)}')
    print(trem[2])
    # entrando na exceção
    print(trem[5])
