from enum import Enum, unique

from util import gerador

@unique
class EstadoDoTerreno(Enum):
    VAZIO = 0
    FIXADO = 1
    COLOCADO = 3

class Tabuleiro():
    def __init__(self):
        self.estado = gerador(4, gerador(4, lambda: EstadoDoTerreno.VAZIO))()