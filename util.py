import markovify
from os import getcwd, mkdir
from os.path import isdir
import io


# Turns lines into sentences that markovify can parse.
def get_text_model(lines):
    for i in range(len(lines)):
        line = ""
        for j in range(len(lines[i])):
            line += lines[i][j]
            if j < len(lines[i]) - 1:
                line += " "
            else:
                line += "."
        lines[i] = line
    text_model = markovify.Text(lines, state_size=2)
    return text_model


# Returns a scrambled markovified word.
def markov(text_model):
    sentence = None
    count = 0
    while sentence is None and count < 10:
        sentence = text_model.make_sentence()
        count += 1
    if sentence is None:
        return None, False
    else:
        # Turn the sentence into a word
        return sentence.replace(" ", "").replace(".", "").title(), True


# Generate gibberish.
def generate(filename, filename_suffix, dataset):
    if len(dataset) == 0:
        return
    text_model = get_text_model(dataset)
    added = set()
    generated = []
    for i in range(500):
        item, real = markov(text_model)
        if real and item not in added:
            generated.append(item + "\n")
            added.update({item})
    directory = getcwd() + "/Output"
    if not isdir(directory):
        mkdir(directory)
    with io.open(directory + "/" + filename + "_" + filename_suffix + ".txt", mode="wt", encoding="utf-8") as f:
        f.writelines(generated)
