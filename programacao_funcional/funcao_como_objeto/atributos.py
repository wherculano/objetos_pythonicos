'''Funções e Atributos
Conferindo os atributos e operacoes de objetos do tipo funcao'''


def dobro(x):
    return 2 * x


# verificar atributos da função
print(dir(dobro))

# objetos sao dinamicos.
# print(dobro.n)  # n nao existe, entao dará erro se tentar rodar
dobro.n = 42  # n passa a existir
print(dobro.n)
del dobro.n  # removendo o atributo

n = dobro  # atribuindo a funcao a uma variavel
print(n(3))


#Funcao anonima que faz exatamente a mesma operacao que a dobro acima
dobro2 = lambda x: x * 2

# motivo por ser anonima
print(dobro.__name__)  # >>> 'dobro'
print(dobro2.__name__)  # >>> '<lambda>'