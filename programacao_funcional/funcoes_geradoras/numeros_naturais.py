def gerador_numeros_naturais():
    i = 0
    while True:
        yield i
        i += 1


naturais = gerador_numeros_naturais()

print(next(naturais))
print(next(naturais))
print(next(naturais))

# só gerará um numero "infinito" de numeros naturais se usado no for.
# caso seja apenas utilizado sequencialmente com o next, poderá deixar de usar quando quiser
# continuando iteração dos numeros a partir de onde ele parou
for n in naturais:
    print(n)
    if n == 100:
        break
