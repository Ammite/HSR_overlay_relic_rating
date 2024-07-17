import enum


class RelicSets(enum.Enum):
    BAND_OF_SIZZLING_THUNDER = {
        'name': 'Band of Sizzling Thunder',
        'type': 'relic',
        'parts_names': {
            "head": "Head",
            "hands": "Hands",
            "body": "Body",
            "feet": "Feet"
        },
        'description': '2p: ...; 4p: ...'
        }
    BELOBOG_OF_THE_ARCHITECTS = {
        'name': 'Belobog of the Architects',
        'type': 'planar',
        'parts_names': {
            'planarSphere': 'Planar Sphere',
            'linkRope': 'Link Rope'
        },
        'description': '2p: ...'
    }