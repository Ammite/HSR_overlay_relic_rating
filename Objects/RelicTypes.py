import enum


class RelicTypes(enum.Enum):
    HEAD = {'type': 'head', 'main_stats': []}
    HANDS = {'type': 'hands', 'main_stats': []}
    BODY = {'type': 'body', 'main_stats': []}
    FEET = {'type': 'feet', 'main_stats': []}
    PLANAR_SPHERE = {'type': 'planarSphere', 'main_stats': []}
    LINK_ROPE = {'type': 'linkRope', 'main_stats': []}

