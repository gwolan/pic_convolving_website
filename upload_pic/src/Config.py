from enum import Enum


supported_types = ['jpeg', 'png', 'tga', 'bmp']


class EffectType(Enum):
    BLUR = ('Rozmycie', 1)
    MOTION_BLUR = ('Rozmycie w ruchu', 2)
    EDGE_DETECTION = ('Wykrywanie krawędzi', 3)
    SHARPEN = ('Wyostrzenie', 4)
    EMBOSS = ('Uwypuklenie', 5)

    def __init__(self, effect_name, effect_type):
        self.effect_name = effect_name
        self.effect_type = effect_type
