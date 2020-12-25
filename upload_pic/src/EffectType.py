from enum import Enum


class EffectType(Enum):
    BLUR = ('Rozmycie', 1)
    SHARPEN = ('Wyostrz', 2)
    COLOR_SWAP = ('Odwróć kolory', 3)
    BLACK_AND_WHITE = ('Czarno białe', 4)

    def __init__(self, effect_name, effect_type):
        self.effect_name = effect_name
        self.effect_type = effect_type
