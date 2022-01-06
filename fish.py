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

response = requests.get("http://acnhapi.com/v1/fish/1")
print(response.status_code)
print(createFish(response.json()))
