from os import listdir, getcwd
from json import dumps

provinces = dict()

directory = "c:/program files (x86)/Steam/steamapps/common/Crusader Kings II/history/provinces"

for f in listdir(directory):
    with open(directory + "/" + f, 'rt') as prov:
        lines = prov.readlines()
        title = ""
        culture = ""
        settlements = set()
        for line in lines:
            if line.startswith("title"):
                title = line.split("c_")[1].strip().replace("_", " ").title()
            elif (line.endswith("temple\n") or line.endswith("city\n") or line.endswith("castle\n")) and "{" not in line:
                s = line.split("=")[0].split("b_")[1].strip().replace("_", " ").title()
                settlements.update({s})
            elif line.startswith("culture"):
                culture = line.split(" = ")[1].strip()
        settlements = list(settlements)
        provinces.update({title: {"settlements": settlements, "culture": culture}})

with open(getcwd() + "/provinces.json", "wt") as output:
    output.write(dumps(provinces))

