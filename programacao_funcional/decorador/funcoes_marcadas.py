from programacao_funcional.decorador.registrador import get_marcadas, marcar


def primeira():
    return 2+2


primeira = marcar(primeira)


@marcar  # decorator que faz exatamente a mesma coisa que está acontecendo com a função primeira acima
def segunda():
    return 5+5


if __name__ == '__main__':
    for f in get_marcadas():
        print(f.__name__)
    print(primeira())  # funcao
    print(segunda)  # decorator
    print(primeira)  # decorator (variavel)
