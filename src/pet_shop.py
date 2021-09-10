# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, pets_sold):
    shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    animal = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            animal.append(pet["breed"])
    return animal

def get_pets_by_breed(shop, breed):
    animal = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            animal.append(pet["breed"])
    return animal

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(shop, name):
    pet_to_delete = None
    pet_to_delete = find_pet_by_name(shop, name)
    for pet in shop["pets"]:
        if pet["name"] == name:
            pet_to_delete = pet
            break   
    shop["pets"].remove(pet_to_delete)    


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, money):
    customers["cash"] -= money

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

# OPTIONAL TESTS

def customer_can_afford_pet(customers, new_pet):
    if  customers["cash"] >= new_pet["price"]:
        return True
    return False

# def customer_can_afford_pet(customers, new_pet):
