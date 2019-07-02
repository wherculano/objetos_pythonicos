class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __iter__(self):
        # return (f'vagao #{vagao}' for vagao in range(1, self.num_vagoes + 1)  # funcao geradora.
        for vagao in range(1, self.num_vagoes+1):
            yield f'vagão #{vagao}'


if __name__ == '__main__':
    trem = Trem(5)
    for vagao in trem:
        print(vagao)