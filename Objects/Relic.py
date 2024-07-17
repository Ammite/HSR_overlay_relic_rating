import Objects.MainStats as MainStats
import Objects.SubStats as SubStats

class Relic:
    def __init__(self, level, relic_type, relic_set):
        self.level = level

        self.relic_type = relic_type
        self.relic_set = relic_set

        self.main_stat = None
        self.sub_stats = None
        '''
        calculate sub_stats
        maybe sub_stats is dict, maybe class
        {
            "first": {
                "sub_stat": SubStats.SPD,
                "sub_stat_roll": 1
                },
            "second": {
                "sub_stat": SubStats.SPD,
                "sub_stat_roll": 1
                },
            "third": {
                "sub_stat": SubStats.SPD,
                "sub_stat_roll": 1
                },
            "fourth": {
                "sub_stat": SubStats.SPD,
                "sub_stat_roll": 0
                }
        }
        '''