from dataclasses import dataclass, field
import requests

@dataclass
class Sea_Creature:
    id: int
    name: dict
    availability: dict
    speed: str
    shadow: str
    price: int
    catch_phrase: str
    museum_phrase: str

    def __str__(self):
        result = ""
        result += "%s: \"%s\"\n" % (self.name["name-USen"], self.catch_phrase)
        result += "Sell for %u\n" % self.price
        result += "%s\n" % self.museum_phrase
        return result

def createSeaCreature(creature_dict):
    id = creature_dict["id"]
    name = creature_dict["name"]
    availability = creature_dict["availability"]
    speed = creature_dict["speed"]
    shadow = creature_dict["shadow"]
    price = creature_dict["price"]
    catch_phrase = creature_dict["catch-phrase"]
    museum_phrase = creature_dict["museum-phrase"]
    return Sea_Creature(id,name,availability,speed,shadow,price,catch_phrase,museum_phrase)

def createSeaCreatures(creatures_dict):
    return map(createSeaCreature,list(creatures_dict.values()))

response = requests.get("http://acnhapi.com/v1/sea")
print(response.status_code)
creatures = createSeaCreatures(response.json())
for creature in creatures:
    print(creature)