import abc


class Bicicleta(abc.ABC):
    _marca = 'Caloi'  # atributos da classe

    def __init__(self):
        self._velocidade = 0  # atributo de instancia. Relacionado a instancia

    @classmethod  # metodo da classe. Independe da instancia
    def marca(cls):  # cls = Receber a propria classe (Bicicleta) e nao a instancia (self)
        return cls._marca

    # Encapsulamento (Get e Set)
    @property  # protege o atributo e o deixa disponivel apenas para leitura (get)
    def velocidade(self):
        return self._velocidade

    @velocidade.setter  # habilita o atributo para seu valor poder ser alterado
    def velocidade(self, valor):
        if valor >= 0:
            self._velocidade = valor
        else:
            self._velocidade = 0

    # @x.deleter é usado para poder deletar o atributo da variavel x

    # metodos abstratos que precisam ser sobrescritos nas subclasses de Bicicleta.
    def pedalar(self):  # contrato informal. Nao obriga implementar o metodo caso ele nao seja utilizado
        """Cada classe concreta deve definir o metodo pedalar com seu incremento na velocidade"""
        raise NotImplementedError()

    @abc.abstractmethod  # contrato formal que obriga a subclasse implementar o metodo
    def frear(self):
        """Cada classe concreta deve definir o metodo frear com seu decremento na velocidade"""
        # raise NotImplementedError()


class Monark(Bicicleta):
    _marca = 'Monark'  # atributos protegidos podem ser acessados e sobrescritos nas subclasses

    def pedalar(self):
        self._velocidade += 10

    #  Tirar os comentarios deste metodo pois ele é obrigado a ser implementado
    def frear(self):
        self._velocidade -= 3


if __name__ == '__main__':
    bicicleta = Monark()
    print(Bicicleta.marca())
    print(Monark.marca())
    print(bicicleta.marca())
    bicicleta.pedalar()
    bicicleta.frear()
    bicicleta.frear()
    print(bicicleta.velocidade)
    bicicleta.velocidade = -4
    print(bicicleta.velocidade)
