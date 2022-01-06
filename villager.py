from dataclasses import dataclass, field

@dataclass
class Villager:
    id: int
    image_file: str
    name: dict
    personality: str
    birthday: str # e.g. 8/18
    birthday_string: str # e.g. August 18th
    species: str
    gender: str
    catch_phrase: str