_marcadas = []


def get_marcadas():
    return _marcadas


def marcar(f):
    _marcadas.append(f)
    return f
