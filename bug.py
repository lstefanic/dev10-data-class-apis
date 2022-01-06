from dataclasses import dataclass, field
import requests

@dataclass
class Bugs:
    id: int
    name: dict
    availability: dict
    price: int
    price_flick: int
    catch_phrase: str
    museum_phrase: str

def createBug(bug_dict):
    id = bug_dict["id"]
    name = bug_dict["name"]
    availability = bug_dict["availability"]
    price = bug_dict["price"]
    price_flick = bug_dict["price-flick"]
    catch_phrase = bug_dict["catch-phrase"]
    museum_phrase = bug_dict["museum-phrase"]
    return Bugs(id,name,availability,price,price_flick,catch_phrase,museum_phrase)

def createBugs(bugs_dict):
    return map(createBug,list(bugs_dict.values()))

response = requests.get("http://acnhapi.com/v1/bugs")
print(response.status_code)
bugs = createBugs(response.json())
for bug in bugs:
    print(bug)        
