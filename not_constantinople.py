from os import getcwd, listdir
from json import loads
import io
from util import generate


# Returns all provinces and their settlements with a given culture.
def get_culture(culture):
    with io.open(getcwd() + "/provinces.json", mode='rt', encoding="utf-8") as f:
        provinces = loads(f.read())
        c_p = dict()
        for key in provinces.keys():
            if provinces[key]["culture"] == culture:
                c_p.update({key: provinces[key]})
        return c_p


# Returns all provinces with a given culture.
def get_provinces(culture):
    provinces = []
    for key in culture.keys():
        p = get_culture(key).keys()
        for i in range(culture[key]):
            provinces.extend(p)
    return provinces


# Returns all settlements with a given culture.
def get_settlements(culture):
    settlements = []
    for key in culture.keys():
        s = get_culture(key)
        for k in s.keys():
            settlements.extend(s[k]["settlements"])
    return settlements


# Load the stored cultural blends and generate some names.
for f in listdir(getcwd() + "/Input"):
    with io.open(getcwd() + "/Input/" + f, mode="rt", encoding="utf-8") as j:
        # Get the saved cultural blend.
        json_culture = loads(j.read())
        # Generate names of provinces and settlements.
        generate(json_culture["name"], "provinces", get_provinces(json_culture["culture"]))
        generate(json_culture["name"], "settlements", get_settlements(json_culture["culture"]))
