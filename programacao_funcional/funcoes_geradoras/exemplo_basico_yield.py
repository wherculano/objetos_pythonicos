def funcao_geradora():
    print('Inicio')
    yield 1  # será executado até aqui até que a funcao seja chamada novamente (com next)
    yield 2
    yield 3
    print('Fim')


gerador = funcao_geradora()

# o laço for trata a exceção StopIteration e nao a retorna ao fim do laço
for i in funcao_geradora():  # ou for in gerador (mas os prints abaixo nao funcionariam mais)
    print(i)

print('-'*20)
print(gerador)
print(next(gerador))
print(next(gerador))
print(next(gerador))
# aqui a exceção StopIteration será lançada pois não haverá mais nenhum yield para ser retornado
# após consumir o conteudo de um gerador não é mais possivel fazer a sua chamada
# print(next(gerador)
