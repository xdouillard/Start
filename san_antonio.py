import random
import json

#quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
# characters = ["alvin et les Chipmunks", "Babar", "betty Boop", "calimero", "casper", "Le chat Potté", "Kirikou"]

# Read values from a JSON file
def read_value_from_json(file, key):
    values =[]
    # Open a json file with my objects
    with open(file) as f:
        # Load all the data contained in my file. data = entries
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return  item # return the item

def get_random_quote():
    all_values = read_value_from_json('quotes.json', 'quote')
    return get_random_item_in(all_values)

def get_random_character():
    all_values = read_value_from_json('characters.json', 'character')
    return get_random_item_in(all_values)

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter.")

while user_answer != "B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter.")