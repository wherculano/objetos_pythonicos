# Usando funcao de alta ordem para facilitar uma Ordenacao

alunos = [('Bianca', 16), ('Winicius', 11), ('Guilherme', 9)]

# ordenando a lista por idade usando a funcao anonima
alunos.sort(key=lambda aluno: aluno[1])
print(alunos)


def por_nome(aluno):
    return aluno[0]


# (sorted) cria uma segunda lista ordenada baseado no iterável passado
print(sorted(alunos, key=por_nome))
