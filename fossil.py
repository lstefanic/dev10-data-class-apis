from dataclasses import dataclass, field
import requests

@dataclass
class Fossil:
    name: dict
    price: int
    museum_phrase: str

def createFossil(fossil_dict):
    name = fossil_dict["name"]
    price = fossil_dict["price"]
    museum_phrase = fossil_dict["museum-phrase"]
    return Fossil(name,price,museum_phrase)

def createFossils(fossils_dict):
    return map(createFossil,list(fossils_dict.values()))

response = requests.get("http://acnhapi.com/v1/fossils")
print(response.status_code)
fossils = createFossils(response.json())
for fossil in fossils:
    print(fossil)