import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
characters = ["alvin et les Chipmunks", "Babar", "betty Boop", "calimero", "casper", "Le chat Potté", "Kirikou"]

def get_random_item(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return  item # return the item

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter.")

while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes)))
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter.")