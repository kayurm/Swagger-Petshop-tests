from main.Pet_simple import Pet
import pytest
import random
import string


@pytest.fixture(scope="module")
def supply_pet_data():
    pet_id = random.randint(60000, 80000)
    categ_name = ''.join(random.choices(string.ascii_letters, k=10))
    pet_name = ''.join(random.choices(string.ascii_letters, k=20))
    status_set = ("available", "pending", "sold")
    status = random.choice(status_set)
    tag_name = ''.join(random.choices(string.ascii_letters, k=20))
    photo_url = "https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/1500925839-golden-retriever-puppy.jpg]"

    return [pet_id, categ_name, pet_name, status, tag_name, photo_url]


@pytest.fixture(scope="module")
def instantiate_pet(supply_pet_data):
    new_pet = Pet(supply_pet_data[0], supply_pet_data[1], supply_pet_data[2],
                  supply_pet_data[3], supply_pet_data[4], supply_pet_data[5])
    return new_pet

@pytest.fixture(scope="module")
def post_new_pet(instantiate_pet):
    pet = instantiate_pet
    return pet.create_pet()

def test_post_new_pet(post_new_pet):
    assert post_new_pet

def test_update_pet(instantiate_pet):
    pet = instantiate_pet
    categ_name = ''.join(random.choices(string.ascii_letters, k=10))
    pet_name = ''.join(random.choices(string.ascii_letters, k=20))
    status_set = ("available", "pending", "sold")
    status = random.choice(status_set)
    tag_name = ''.join(random.choices(string.ascii_letters, k=20))
    photo_url = "https://i.stack.imgur.com/DmgRr.png"
    assert pet.update_pet(categ_name, pet_name, status, tag_name, photo_url)

def test_get_pet(instantiate_pet):
    pet = instantiate_pet
    assert pet.get_pet() == 200

def test_delete_pet(instantiate_pet):
    pet = instantiate_pet
    assert pet.delete_pet() == 200


