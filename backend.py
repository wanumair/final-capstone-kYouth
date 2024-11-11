import requests

def create_random_user():
    url = "https://randomuser.me/api/?inc=name"
    response = requests.get(url)
    first_name = response.json()['results'][0]['name']['first']
    last_name = response.json()['results'][0]['name']['last']

    user_data = first_name + " " + last_name
    return user_data

def generate_fruit_data(fruit):
    url = f"https://www.fruityvice.com/api/fruit/{fruit}"
    response = requests.get(url)
    raw_fruit_data = response.json()['nutritions']
    fruit_calories = raw_fruit_data['calories']
    fruit_fat = raw_fruit_data['fat']
    fruit_sugar = raw_fruit_data['sugar']
    fruit_carbohydrates = raw_fruit_data['carbohydrates']
    fruit_protein = raw_fruit_data['protein']
    fruit_data = f"{fruit}'s has calories of {fruit_calories}%, the fat is {fruit_fat}%, while the sugar is {fruit_sugar}%, the protein is {fruit_protein}% and the carbs is {fruit_carbohydrates}% of the fruit."
    return fruit_data


def birthday_fact(date):
    #keyin date
    url = f"http://numbersapi.com/{date}/date?json"
    response = requests.get(url)
    date_fact = response.json()['text']
    return date_fact

def get_harry_potter_facts(number_of_book):   
    # number_of_book = int(input("Which harry potter books is your favorite:"))
    url = "https://potterapi-fedeperin.vercel.app/en/books"
    response = requests.get(url)
    book_title = response.json()[number_of_book - 1]['title']
    book_description = response.json()[number_of_book - 1]['description']
    book_release= response.json()[number_of_book - 1]['releaseDate']
    book_pages= response.json()[number_of_book - 1]['pages']
    book_image= response.json()[number_of_book - 1]['cover']
    harry_potter_book = "The tittle of the book is:"+ " " + book_title + ' \n' + "The story is about..."+ " " + book_description +" \n" + f"{book_title} has {book_pages} of pages and released on {book_release}"
    return harry_potter_book, book_image


def get_harry_potter_char_facts(user_input):
    url = "https://potterapi-fedeperin.vercel.app/en/characters"
    response = requests.get(url)
    list_of_char = response.json()[user_input - 1]
    # print(list_of_char)
    char_name = list_of_char['fullName']
    char_house = list_of_char['hogwartsHouse']
    char_actor = list_of_char['interpretedBy']
    char_kids = list_of_char['children']
    image = list_of_char['image']
    
    name_kids = ''
    
    for char in char_kids:
        name_kids= name_kids + ', ' + char
    if char_kids == []:
        name_kids= 0
    about_char = f"Character that you are interested with is: {char_name}. {char_name} is in {char_house}'s house and being acted by {char_actor}. {char_name} has {name_kids}  as kids in the movies."
    return about_char, image


def hp_spells(index):
    url = f"https://potterapi-fedeperin.vercel.app/en/spells/?index={index}"
    response = requests.get(url)
    name_spell = response.json()['spell']
    use_spell = response.json()['use']
    return name_spell, use_spell

