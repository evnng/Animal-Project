import json
from functions import get_access_token, get_animal_types, get_animals_by_type, \
                     get_animals_dataset, print_babies_adults, print_animal_types, \
                     digit_check, string_check, string_check_1, add_animal, info_about_pet


with open('data.json') as infile:
    dataset = json.load(infile)

    print("Welcome to the Pet Project!")
while True:
    
    print( "Enter your option:\n",
          "Enter 1 if you want to see all possible types of animals\n",
          "Enter 2 if you want to delete adopted animal\n",
          "Enter 3 if you want to add new animal to dataset\n",
          "Enter 4 if you want to update data from the website\n",
          "Enter 5 if you want to exit the programm\n")

    option1 = digit_check(5, 1)

    if option1 == 1:
        while True:
            print_animal_types(dataset)

            print("   Enter 1 if you want to adopt animal of some type\n",
                  "  Enter 2 if you want to exit to the main menu")

            option2 = digit_check(2, 1)

            if option2 == 1:

                type_animal = string_check(dataset, "Enter, animal of what type you would like to adopt: ")

                print_babies_adults(dataset, type_animal)

                name_adopt = string_check(dataset[type_animal], "Enter name of animal which characteristics you would like to see: ")

                info_about_pet(dataset, type_animal, name_adopt)
                
                answer = string_check_1("Yes", "No", "Do you confirm that you want to adopt this pet? Enter Yes or No: ")

                if answer == "Yes":
                    del dataset[type_animal][name_adopt]

            if option2 == 2:
                break

    if option1 == 2:

        while True:

            print("   Enter 1 if you want to delete pet from the dataset\n",
                  "  Enter 2 if you want to exit to the main menu\n")

            option3 = digit_check(2, 1)

            if option3 == 1:

                print_animal_types(dataset)

                type_delete = string_check(dataset, "Enter, animal of what type you would like to delete from the dataset: ")

                print_babies_adults(dataset, type_delete)

                name_delete = string_check(dataset[type_delete], "Enter name of animal which you want to delete: ")

                del dataset[type_delete][name_delete]

            if option3 == 2:
                break

    if option1 == 3:
        
        while True:
            
            print("   Enter 1 if you want to add pet to the dataset\n",
                  "  Enter 2 if you want to exit to the main menu\n")
            
            option4 = digit_check(2, 1)
            
            if option4 == 1:
                
                print_animal_types(dataset) 
                type_add = string_check(dataset, "Enter, animal of what type you would like to add to the dataset: ")
                name_add = add_animal(dataset, type_add)

                info_about_pet(dataset, type_add, name_add)
                print("\n")
                
            else:
                break
    
    if option1 == 4:
        token   = get_access_token()
        types   = get_animal_types(token)
        dataset = get_animals_dataset(types, token)
        print("Data was successfully updated! \n")
            
    if option1 == 5:
        break
        
with open('data.json', 'w') as outfile:
    json.dump(dataset, outfile)
