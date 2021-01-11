from enum import Enum


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_FILE_SIZE_BYTES = 10485760
MAX_FILE_SIZE_MB = 10


engine_error_codes = {
    1: "Błąd serwera. Nie udało się wczytać pliku",
    2: "Błąd serwera. Nie udało się zapisać przetworzonego pliku"
}


file_life_time_secs = 60
file_queue_supervisor_wait_time_secs = 2


supported_types = ['jpeg', 'png', 'tga', 'bmp']


class EffectType(Enum):
    BLUR = ('Rozmycie', 1)
    MOTION_BLUR = ('Rozmycie w ruchu', 2)
    EDGE_DETECTION = ('Wykrywanie krawędzi', 3)
    SHARPEN = ('Wyostrzenie', 4)
    EMBOSS = ('Ukazanie wypukłości', 5)

    def __init__(self, effect_name, effect_type):
        self.effect_name = effect_name
        self.effect_type = effect_type
