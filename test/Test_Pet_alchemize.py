import main.Pet_alchemize as PetApi
import pytest
import random
import string


@pytest.fixture(scope="module")
def supply_pet_data():
    pet_id = random.randint(60000, 80000)
    categ_name = ''.join(random.choices(string.ascii_letters, k=10))
    categ_id = random.randint(1, 100)
    pet_name = ''.join(random.choices(string.ascii_letters, k=10))
    status_set = ("available", "pending", "sold")
    status = random.choice(status_set)
    tag_id = random.randint(1, 100)
    tag_name = ''.join(random.choices(string.ascii_letters, k=5))
    photo_url1 = ["https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/1500925839-golden-retriever-puppy.jpg"]
    return [pet_id, categ_id, categ_name, pet_name, photo_url1, tag_id, tag_name, status]


@pytest.fixture(scope="module")
def instantiate_pet(supply_pet_data):
    new_pet = PetApi.Pet(supply_pet_data[0], supply_pet_data[1], supply_pet_data[2],
                         supply_pet_data[3], supply_pet_data[4], supply_pet_data[5], supply_pet_data[6],
                         supply_pet_data[7])
    return new_pet


@pytest.fixture(scope="module")
def post_new_pet(instantiate_pet):
    return PetApi.register_pet(instantiate_pet)


def test_post_new_pet(post_new_pet, supply_pet_data):
    assert post_new_pet is not None
    assert post_new_pet["id"] == supply_pet_data[0], "request pet_id not equal to response pet_id"
    assert post_new_pet["name"] == supply_pet_data[3], "request pet_id not equal to response pet_id"


def test_update_pet(supply_pet_data):
    pet_id = supply_pet_data[0]
    categ_name = ''.join(random.choices(string.ascii_letters, k=10))
    categ_id = random.randint(1, 100)
    pet_name = ''.join(random.choices(string.ascii_letters, k=20))
    status_set = ("available", "pending", "sold")
    status = random.choice(status_set)
    tag_id = random.randint(1, 100)
    tag_name = ''.join(random.choices(string.ascii_letters, k=5))
    photo_url = "https://i.stack.imgur.com/DmgRr.png"

    pet_update = PetApi.update_pet(
        PetApi.Pet(pet_id, categ_id, categ_name, pet_name, photo_url, tag_id, tag_name, status))
    assert pet_update is not None
    assert pet_update["id"] == pet_id
    assert pet_update["name"] == pet_name
    assert pet_update["status"] == status
    assert pet_update["category"]["id"] == categ_id


def test_get_pet(supply_pet_data):
    get_pet_info = PetApi.GetPetInfo(supply_pet_data[0])
    assert get_pet_info == 200


def test_delete_pet(supply_pet_data):
    delete_pet = PetApi.DeletePet(supply_pet_data[0])
    assert delete_pet == 200
