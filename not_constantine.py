from os import getcwd, listdir
from json import loads
import io
from util import generate


# Returns all provinces and their settlements with a given culture.
def get_names_json():
    with io.open(getcwd() + "/names.json", mode='rt', encoding="utf-8") as f:
        return loads(f.read())


# Returns the names of a given key (male, female, surnames) a certain amount of times, given the input blend.
def get_names(full_data, input_json, key):
    names = []
    for culture in input_json["culture"].keys():
        if culture not in full_data.keys():
            continue
        for i in range(input_json["culture"][culture]):
            names.extend(full_data[culture][key])
    return names


names_data = get_names_json()

# Load the stored cultural blends and generate some names.
for f in listdir(getcwd() + "/Input"):
    with io.open(getcwd() + "/Input/" + f, mode="rt", encoding="utf-8") as j:
        # Get the saved cultural blend.
        json_culture = loads(j.read())
        # Generate names of provinces and settlements.
        generate(json_culture["name"], "forenames_male", get_names(names_data, json_culture, "male"))
        generate(json_culture["name"], "forenames_female", get_names(names_data, json_culture, "female"))
        generate(json_culture["name"], "surnames", get_names(names_data, json_culture, "surnames"))
