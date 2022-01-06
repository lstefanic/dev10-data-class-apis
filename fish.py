from dataclasses import dataclass, field
import requests

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

    def __str__(self):
        result = ""
        result += "%s: \"%s\"\n" % (self.name["name-USen"], self.catch_phrase)
        result += "Buy for %u, or buy from CJ for %u\n" % (self.price, self.price_cj)
        result += "%s\n" % self.museum_phrase
        return result

def createFish(fish_dict):
    id = fish_dict["id"]
    name = fish_dict["name"]
    availability = fish_dict["availability"]
    shadow = fish_dict["shadow"]
    price = fish_dict["price"]
    price_cj = fish_dict["price-cj"]
    catch_phrase = fish_dict["catch-phrase"]
    museum_phrase = fish_dict["museum-phrase"]
    return Fish(id,name,availability,shadow,price,price_cj,catch_phrase,museum_phrase)

def createFishes(fishes_dict):
    return map(createFish,list(fishes_dict.values()))

response = requests.get("http://acnhapi.com/v1/fish")
print(response.status_code)
fishes = createFishes(response.json())
for fish in fishes:
    print(fish)
