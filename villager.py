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

    def __str__(self):
        result = ""
        result += "%s: \"%s\"\n" % (self.name["name-USen"], self.catch_phrase)
        result += "%s, %s, %s\n" % (self.species, self.gender, self.personality)
        result += "Born on %s\n" % self.birthday_string
        return result

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

def createVillagers(villagers_dict):
    return map(createVillager,list(villagers_dict.values()))

response = requests.get("http://acnhapi.com/v1/villagers")
print(response.status_code)
villagers = createVillagers(response.json())
for villager in villagers:
    print(villager)