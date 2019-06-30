alunos = [('Bianca', 16), ('Winicius', 11), ('Guilherme', 9)]

# filtrar idade acima de 10 anos utilizando list comprehension
print([(nome, idade) for nome, idade in alunos if idade > 10])


# filtrar utilizando o método filter
# recebe uma funcao que recebera cada um dos elementos de um iteravel que deve ser passado como segundo parametro
def idade_maior_que_10(aluno):
    _, idade = aluno  # fazendo o desempacotamento. O _ ignora o elemento que nao deseja receber, no caso Nome
    return idade > 10


print(list(filter(idade_maior_que_10, alunos)))


def extrair_nome(aluno):
    nome, _ = aluno
    return nome

# Mapear e filtrar os nomes com idade maior que 10 anos
print(list(map(extrair_nome, filter(idade_maior_que_10, alunos))))

# Modulo Operator para fazer a mesma coisa
import operator
print(list(map(operator.itemgetter(0), filter(idade_maior_que_10, alunos))))
# operator.itemgetter pega o elemento de um iteravel pelo seu indice. Neste caso acima, pegará o primeiro elemento (0)
