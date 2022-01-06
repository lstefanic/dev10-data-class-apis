from dataclasses import dataclass, field

@dataclass
class Bugs:
    id: int
    name: dict
    availability: dict
    price: int
    price_flick: int
    catch_phrase: str
    museum_phrase: str