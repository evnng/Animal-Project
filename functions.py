import json
import requests


# Create a function that gets API Access Token before importing data
def get_access_token():
    client_id = 'ENLBz9qOmYCW2MnQO2qVkfM9mBHmHEQP3LgXp9XNxKPwNwkYWE'
    client_secret = 'mD9hlx3QIeBLqvLHvHSF3TWzjRBj0aqdQlMdNXeT'
    url = 'https://api.petfinder.com/v2/oauth2/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    token = requests.post(url, params).json()['access_token']
    return token


# Create a function that gets available animal types
def get_animal_types(token):
    url = 'https://api.petfinder.com/v2/types'
    head = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=head).json()
    types = []
    for type_animal in response['types']:
        types.append(type_animal['name'])
    return types


# Create a function that returns a tuple with 20 animals of certain type
def get_animals_by_type(type_animal, token):
    url = 'https://api.petfinder.com/v2/animals'
    head = {'Authorization': 'Bearer ' + token}
    params = {'type': type_animal}
    response = requests.get(url, headers=head, params=params).json()
    data = {}
    for animal in response['animals']:
        data[animal['id']] = {
            'type': animal['type'],
            'name': animal['name'],
            'age': animal['age'],
            'color': animal['colors']['primary'],
            'gender': animal['gender'],
            'size': animal['size'],
            'status': animal['status'],
            'contact_email': animal['contact']['email'],
            'contact_phone': animal['contact']['phone']
        }
    return data


# Create a function that generates dataset with animals of all available types
def get_animals_dataset(types, token):
    dataset = {}
    for type_animal in types:
        data = get_animals_by_type(type_animal, token)
        data_type = {}
        for k in data:
            data_type[data[k]['name']] = data[k]
        for name in data_type:
            del data_type[name]['name']
            del data_type[name]['type']
        dataset[type_animal] = data_type
    return dataset


# Create a function that print names of certain animals with sort by age
def print_babies_adults(data, type_animal):
    print('\n')
    print(f'Here you can see {type_animal} Babies: ')

    for name in data[type_animal]:
        if data[type_animal][name]['age'] == 'Baby':
            print(name, end='; ')
    print('\n')

    print(f'Here you can see {type_animal} Adults: ')

    for name in data[type_animal]:
        if data[type_animal][name]['age'] == 'Adult':
            print(name, end='; ')
    print('\n')


# Create a function that print all types of animals in the dataset
def print_animal_types(dataset):
    print("Animal types:")
    for type_animal in dataset:
        print(type_animal, end='; ')
    print("\n")


# Create a function that check, if digit suit some conditions
def digit_check(higher_border, lower_border):
    while True:
        option = input()
        if option.isdigit() == False or int(option) >= higher_border + 1 or int(option) < lower_border:
            print("Entered value is not a correct option. Please, try again.")
        else:
            option = int(option)
            return option
            break


# Creates a function that chenk if string is in the dataset
def string_check(data, message):
    while True:
        string = input(message)
        if not (string in data):
            print("Entered value is not a correct option. Please, try again.")
        else:
            return string
            break


# Create a function that check, if string suit some conditions
def string_check_1(option1, option2, message):
    while True:
        answer = input(message)
        if not (answer == option1 or answer == option2):
            print("Entered value is not a correct option. Please, try again.")
        else:
            return (answer)
            break


# Create a fuction that add animal to the dataset
def add_animal(data, type_animal):
    name = input("Enter name of the pet: ")
    age = string_check_1("Baby", "Adult", "Enter age of the pet: Baby or Adult: ")
    color = input("Enter color/colors of the pet: ")
    gender = string_check_1("Male", "Female", "Enter gender of the pet: Male or Female: ")
    size = input("Enter size of the pet: ")
    status = string_check_1("adoptable", "non-adoptable", "Enter atatus of the pet: adoptable or non-adoptable: ")
    contact_email = input("Enter your contact email: ")
    contact_phone = input("Enter your contact phone: ")
    data[type_animal][name] = {'age': age, 'color': color, 'gender': gender, 'size': size, 'status': status,
                               'contact_email': contact_email, 'contact_phone': contact_phone}
    return name


# Create a function that print information about pet
def info_about_pet(dataset, type_animal, name):
    for line in dataset[type_animal][name]:
        print(line, ":", dataset[type_animal][name][line])
