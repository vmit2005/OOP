import json
from random import choice
# from ramка import Ramка as R
# R(40,"OOP14","Домашнее задание")


def get_person():
    primary_key=''
    name = ''
    tel = ''
    letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(primary_key) != 10:
        primary_key += choice(nums)
    while len(name) != 7:
        name += choice(letter)
    while len(tel) != 10:
        tel += choice(nums)

    person = { primary_key:{
        'name': name,
        'tel': tel
    }
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)



for i in range(5):
    write_json(get_person())
