
# Overview
**Not Constantinople** randomly generates city and regional names based on real-life cities. Want a fantasy city name that sounds English but with some French and Italian thrown in? That's what this program does.

Here is "Lyria", a blend of Visigothic, Saxon, and Suebi:

![Lyria](/Images/lyria.png)

And here is "Pharostine", a blend of Assyrian, Georgian, Alan, Greek, Roman, and Armenian:

![Pharostine](/Images/pharostine.png)

# About this manual
This manual is intended for _non-programmers_. If you're a non-programmer, this all might appear a little intimidating. That's OK. I promise it looks tougher to use than it actually is. I'm going to walk you through installing and using the program. Have confidence in your own abilities! It'll be great!

# License
See [license.txt](license.txt)

The content of `provinces.json` was scraped from the data files of the video game Crusader Kings II.

# Installation

## 1. Install Python 3
Grab it [here](https://www.python.org/downloads/) (Click the big yellow button).

When installing, be sure to _Add Python to PATH_ (the checkbox at the very bottom).
![The Python path checkbox is at the bottom of the dialogue box](Images/python_install.png)

### What is Python?
Python is a programming language. I made this software in Python. Python is a good tool for some things and not a good tool for other things. It's a _great_ tool for doing zany stuff with words.

I could _compile_ it into a .exe or .app, but I don't think it's worth it--for example, I don't own a Mac, so I would have no way to know if it actually works on OS X. If I just leave it as Python code, I can be sure it'll work for you.

## 2. Open up the terminal
In Windows, go to Start, click on the search dialogue, type in `cmd`, and press enter.

In OS X, go to finder, type in `terminal`, and press enter.

Congrats! You're in the Matrix. The terminal looks way scarier than it actually is.

### How to read terminal instructions
Whenever you read "type `some instructions`" that always means: type those instructions _in the terminal_ and then _press enter._

Whenever you read something like "type `cd <path/to/file>`" don't type the \< or the \>, and replace path/to/file with the actual path to the file (for example: `cd c:/users/seth/Not_Constantinople`)  

## 3. Install stuff with pip
You just need to have an extra Python thing:
type `pip -3.6 install markovify`

## 4. Download my program
Get it [here](https://github.com/subalterngames/Not_Constantinople/releases/tag/1.0). Unzip the download.

## 5. Congratulate yourself!
OK you're all set up. Great job!! I knew you could do it.  

# Usage

Using Windows Explorer (Windows) or Finder (OS X), navigate to `Not_Constantinople/Input` (I don't know where the folder ``Not_Constantinople` is located; it's wherever you unzipped the download .zip file.)

## Input

I've included a couple sample input files in `Cultural_Name_Place_Generator/Input` They are all `.json` files. You can open them in Notepad on Windows and TextEdit in OS X. They look like this:

```
{
    "culture": {
        "assyrian": 1,
        "georgian": 1,
        "alan": 1,
        "greek": 15,
        "roman": 8,
        "armenian": 8
    },
    "name": "pharostine"
}

```
`name` is the name of the _fantasy_ culture. `culture` is the pre-set names of cultures that can blend together. The number is the `weight`. A higher number means that this culture's place-names will be favored more.

You can use the examples I provided to create your own; just remember to save them to the `Input` folder, and make sure the extension is `.json` instead of `.txt`

See "Cultures" for the list of acceptable cultures.

## Output

Once you have set up your fantasy culture(s), open the terminal.

- type `cd <path/to/Not_Constantinople`
- type `py -3.6 namer.py`

Wait a bit for the terminal prompt to re-appear... that's how you'll know it's done processing.

Go to the `Output` folder. There's your placenames!

- **Settlements** are names of towns or cities
- **Provinces** are names of regions, kingdoms, etc.

# Cultures
These are the accepted names of cultures:

- pommeranian
- manden
- greek
- khazar
- serbian
- persian
- saka
- assamese
- alan
- norse
- polish
- sindhi
- hindustani
- egyptian_arabic
- telugu
- lappish
- karluk
- sumpa
- occitan
- bohemian
- hungarian
- komi
- welsh
- assyrian
- khanty
- sinhala
- avar
- gujurati
- breton
- croatian
- old_saxon
- romanian
- georgian
- cuman
- ethiopian
- bulgarian
- baloch
- german
- tocharian
- kannada
- lombard
- maghreb_arabic
- turkish
- nepali
- bengali
- panjabi
- tangut
- irish
- ugricbaltic
- marathi
- basque
- suebi
- pictish
- bolghar
- lithuanian
- visigothic
- kirghiz
- severian
- lettigallish
- nubian
- bedouin_arabic
- oriya
- levantine_arabic
- samoyed
- ilmenian
- mordvin
- tamil
- italian
- afghan
- sogdian
- zhangzhung
- prussian
- pecheneg
- saxon
- han
- old_frankish
- bodpa
- finnish
- volhynian
- frisian
- somali
- kurdish
- armenian
- uyghur
- rajput
