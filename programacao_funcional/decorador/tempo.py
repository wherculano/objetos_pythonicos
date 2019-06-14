from functools import wraps
from time import strftime, sleep
from decorator import decorator, getfullargspec
# criando decorators com parametros opcionais


# # o * obriga a funcao a receber os parametros de forma nomeada
# esta funcao decorada não utiliza a lib decorator. Mas é uma forma mais detalhada/complexa de como ele funciona
# def logar(fn=None, *, fmt='%H:%M:%S'):  # fn=funcao a ser decorada
#     if fn is not None:
#         return logar(fmt=fmt)(fn)
#
#     def decorator(f):
#         @wraps(f)  # ajusta o __name__ (entre outros parametros) para bater com a funcao original q está sendo passada
#         def executar_com_tempo(*arg, **kwargs):
#             print(strftime(fmt))
#             return f(*arg, **kwargs)
#
#         return executar_com_tempo
#
#     return decorator

@decorator
def logar(f, fmt='%H:%M:%S', *args, **kwargs):  # f=funcao a ser decorada
        print(strftime(fmt))
        return f(*args, **kwargs)


@logar  # para a logar sem o decorator 'decorator', logar(fn=mochileiro) - funcao toda comentada
def mochileiro():
    return 42


@logar(fmt='%d/%m/%Y %H:%M:%S')  # fn=None
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(getfullargspec(mochileiro))  # retorna os elementos que compoem a especificacao dos argumentos
    print(mochileiro.__name__)  # sem o wraps, os nomes dos objetos estavam sendo retornados como executar_com_tempo
    print(mochileiro())
    print(ola.__name__)
    print(ola('Wagner'))
    print('=-'*10)
    sleep(1)
    print(mochileiro())
    print(ola('Herculano'))
