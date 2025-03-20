from sys import argv
from portfolio.car.car_list import cars


#-------------------------------------------------------------------------------
# This chunk of code chekcs if we want add a car, calls the create_car function, then calls add_car to add it to our list

def check_add_car(car_list):  
    answer = str(input("Do you want to add a car? Y/N \n > "))
    if answer in ["y", "Y", "Yes", "yes", "YES"]: 
        new_car = create_car() 
        add_car(car_list, new_car)
        check_add_car(car_list) 
    else:
        change_car(car_list)

def add_car(car_list, new_car):
    car_list.append([new_car])



def change_car(car_list):
    answer = str(input("Would you like to change a car's details?\n > "))
    if answer in ["y", "Y", "Yes", "yes", "YES"]:
        type = str(input("What would you like to change?\n 'Model'-'Color'-'Speed'\n> "))
        if type in ["Model", "model"]:
            print("You have selected 'Model'")

        if type in ["Color","color"]:
            print("You have selcted 'Color'")

        if type in ["Speed", "speed"]:
            print("You have selected 'Speed'")
            
                
    

    
#-------------------------------------------------------------------------------
# These blocks of functions are the princple for creating any new cars, having sepearte functions for each list/dict parameters

def create_car():   
    new_model = model()
    new_color = color(new_model)
    new_speed = speed(new_model)
    print(f"So you have a {new_color} {new_model} that reaches {new_speed} mph! Nice!")
    
    car = {new_model:
           [{'color': new_color, 
           'speed': new_speed }]
          }
    return car


def model():
    print("What is the model of your car?")
    model_name = input('> ')
    return model_name
    
def color(model_name):
    print(f"What is the color of your {model_name}?")
    color = input('> ')
    return color

def speed(model_name):
    print(f"What is the top speed of the {model_name}")
    speed = int(input('> '))
    return speed

#-------------------------------------------------------------------------------
# Anytime we want to read the entire car list from the console

def read_list(car_list):
    print("\n",car_list,"\n")
    

#-------------------------------------------------------------------------------

check_add_car(cars)
read_list(cars)


# In terms of the Study drill, I think as of current (24/1/25), I am to focused in on saving the dict for later use, when perhaps focusing on building a dict within the same script to the change around will be hitting the target more. 

# To improve this further I could:
# - Edit the list/dict from the console, rather than entering the file manually 
# - Beable to add new dict items, which will then add onto current saved dicts
#     ~ Given option to edit all straight away or to fill with 'none'