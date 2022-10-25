from abc import ABCMeta


class AbstractModelo(metaclass=ABCMeta):
    def __int__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)