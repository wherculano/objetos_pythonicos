a = 5  # variavel em contexto global


def f(a=3):  # 'a' neste escopo local da função é diferente do 'a' global
    b = 3  # variavel local da função e por esse motivo nao se pode acessa-la fora deste escopo local
    print(globals())
    print(locals())
    print(a)  # procurará pela variavel 'a' no escopo local e caso nao a tenha, procurará no escopo global
    print(b)


class A:
    a = 8  # variavel de contexto local da classe e diferente da variavel 'a' global
    a += 1
    print(a)
    print(globals())
    print(locals())


f()
# print(b)  # se tentar executar dará erro pois não temos b declarado no escopo global do módulo
