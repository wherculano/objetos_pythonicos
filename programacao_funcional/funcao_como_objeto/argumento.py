# Funcao como Argumento - Funcao de Alta Order

'''
>>> def ola():
...     print('Olá')
...
>>> executar(ola)
Olá
>>> executar(ola, 2)
Olá
Olá
>>> def ola_mundo():
...     print('Olá, mundo!')
...
>>> executar(ola_mundo, 3)
Olá, mundo!
Olá, mundo!
Olá, mundo!
'''


#Funcao de alta ordem pois recebe outra funcao internamente
def executar(f, n=1):
    for _ in range(n):  #numero de vezes que a funcao devera ser executada
        f()  #executa a funcao que recebeu como parametro


