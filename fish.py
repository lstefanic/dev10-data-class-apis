from dataclasses import dataclass, field

@dataclass
class Fish:
    id: int
    name: dict
    availability: dict
    shadow: str
    price: int
    price_cj: int
    catch_phrase: str
    museum_phrase: str
