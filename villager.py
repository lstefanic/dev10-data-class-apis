from dataclasses import dataclass, field
import requests

@dataclass
class Villager:
    id: int
    name: dict
    personality: str
    birthday: str # e.g. 18/8
    birthday_string: str # e.g. August 18th
    species: str
    gender: str
    catch_phrase: str

def createVillager(villager_dict):
    id = villager_dict["id"]
    name = villager_dict["name"]
    personality = villager_dict["personality"]
    birthday = villager_dict["birthday"]
    birthday_string = villager_dict["birthday-string"]
    species = villager_dict["species"]
    gender = villager_dict["gender"]
    catch_phrase = villager_dict["catch-phrase"]
    return Villager(id,name,personality,birthday,birthday_string,species,gender,catch_phrase)

response = requests.get("http://acnhapi.com/v1/villagers/hip00")
print(response.status_code)
print(createVillager(response.json()))