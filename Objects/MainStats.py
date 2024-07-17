import enum
# https://honkai-star-rail.fandom.com/wiki/Relic/Stats

class MainStats(enum.Enum):
    SPD = {'name': 'Скорость', 'base_value': 0, 'increase_per_level': 0, 'max_value': 0}
    ...