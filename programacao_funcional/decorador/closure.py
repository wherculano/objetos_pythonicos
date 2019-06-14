# def fabrica_de_multiplicadores():
#     def dobro(n):
#         return n*2
#     return dobro
#
#
# dobro_externo = fabrica_de_multiplicadores()
# print(dobro_externo(3))


# closure é o conjunto de valores existentes no escopo da criação de uma função ao qual ela também tem acesso
def fabrica_de_multiplicadores(multiplicador):
    def multiplicar(n):
        return n*multiplicador
    return multiplicar


dobro = fabrica_de_multiplicadores(2)  # 2 será o multiplicador
triplo = fabrica_de_multiplicadores(3)  # 3 será o multiplicador
print(dobro(5))  # o 2 da inicialização de dobro agora multiplicará o 5 recebido (2x5)
print(triplo(8))  # o 3 da inicialização de triplo agora multiplicará o 8 recebido (3x8)
