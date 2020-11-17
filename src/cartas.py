from enum import Enum, unique

@unique
class Terrenos(Enum):
    SAVANA = 1
    PRAIA = 2
    DESERTO = 3
    FLORESTA = 4
    RIO = 5
    # CARVENA: mover requer jogar D6 e > Power(x)
    CARVENA = 6
    MONTANHA = 7

@unique
class Criatura(Enum):
    OVO_DE_AGUIA = 1
    PEIXA = 2
    CACTUS = 3
    LAGOSTA = 4
    ARANHA = 5
    MORCEGO = 6
    CANGURU = 7
    COBRA = 8
    COELHO = 9
    GIRINO = 10

@unique
class Evoluida(Enum):
    LAGOSTA_REI = 1
    SAPO = 2
    NAJA = 3
    CANGURU_MAE = 4

@unique
class Efeito(Enum):
    SONAR = 1
    GEMEOS = 2
    TEIA = 3
    VOAR = 4
    CARDUME = 5
    CHUVA = 6
