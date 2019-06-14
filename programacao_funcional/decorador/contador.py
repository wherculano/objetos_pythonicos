'''
se fosse utilizada uma variavel contador no escopo global e declarado o contador como global ao inves de nonlocal
detro da função contar, este contador seria incrementado sequencialmente, alterando o mesmo objeto, não permitindo que
os contadores (1 e 2) fossem independentes como é o que acontece com o nonlocal.
'''


def fabrica_de_contador():
    contador = 0

    def contar():
        nonlocal contador  # irá acessar uma variável de um contexto externo ao da execução da função contar
        contador += 1
        return contador

    return contar


contador_1 = fabrica_de_contador()
contador_2 = fabrica_de_contador()

print(contador_1())
print(contador_1())
print(contador_1())
print(contador_2())
print(contador_2())