import requests
from alchemize import JsonModel, JsonMappedModel, JsonTransmuter, Attr
from functools import wraps


class Category(JsonMappedModel):
    __mapping__ = {
        'id': Attr('categ_id', int),
        "name": Attr('categ_name', str)
    }

    def __init__(self, categ_id, categ_name, **attrs):
        super().__init__(**attrs)
        self.categ_id = categ_id
        self.categ_name = categ_name


class Tags(JsonMappedModel):
    __mapping__ = {
        "id": Attr('tag_id', int),
        "name": Attr('tag_name', str)
    }

    def __init__(self, tag_id, tag_name, **attrs):
        super().__init__(**attrs)
        self.tag_id = tag_id
        self.tag_name = tag_name


class PhotoUrls(JsonMappedModel):
    __mapping__ = {
        "photoUrls": Attr('photo_url', str)
    }

    def __init__(self, photo_url, **attrs):
        super().__init__(**attrs)
        self.photo_url = photo_url


class Pet(JsonModel):
    __mapping__ = {
        'id': Attr('pet_id', int),
        'category': Attr('category', Category),
        'name': Attr('pet_name', str),
        'status': Attr('status', str),
        'tags': Attr('tags', [Tags]),
        'photoUrls': Attr('photo_url', [PhotoUrls])
    }

    def __init__(self, pet_id, categ_id, categ_name, pet_name, photo_url, tag_id, tag_name, status, **attrs):
        super().__init__(**attrs)
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.status = status
        # self.photo_url = [PhotoUrls(photo_url)]
        self.tags = [Tags(tag_id, tag_name)]
        self.category = Category(categ_id, categ_name)


class PostPetWrap(object):
    def __init__(self, url):
        self.url = url

    def __call__(self, function):
        @wraps(function)
        def wrapper(data_model):
            result_model = JsonTransmuter.transmute_to(data_model)
            req_body = result_model
            res = requests.post(self.url,
                                headers={"Content-Type": "application/json", "accept": "application/json"},
                                data=req_body)

            if res.status_code == 200:
                return res.json()
            else:
                return None

        return wrapper


@PostPetWrap(url='https://petstore.swagger.io/v2/pet/')
def register_pet(pet_data_model):
    return pet_data_model


class GetPetWrap:
    def __init__(self, url):
        self.url = url

    def __call__(self, function):
        @wraps(function)
        def wrapper(pet):
            res = requests.get(f"{self.url}/{pet}")
            return res.status_code

        return wrapper


@GetPetWrap(url='https://petstore.swagger.io/v2/pet')
class GetPetInfo:
    def __init__(self, pet):
        self.pet_id = pet


class UpdatePetWrap:
    def __init__(self, url):
        self.url = url

    def __call__(self, function):
        @wraps(function)
        def wrapper(data_model):
            result_model = JsonTransmuter.transmute_to(data_model)
            req_body = result_model
            res = requests.put(self.url,
                               headers={"Content-Type": "application/json", "accept": "application/json"},
                               data=req_body)
            if res.status_code == 200:
                return res.json()
            else:
                return None

        return wrapper


@UpdatePetWrap(url='https://petstore.swagger.io/v2/pet')
def update_pet(pet_data_model):
    return pet_data_model


class DeletePetWrap:
    def __init__(self, url):
        self.url = url

    def __call__(self, function):
        @wraps(function)
        def wrapper(pet):
            res = requests.delete(f"{self.url}/{pet}")
            return res.status_code

        return wrapper


@DeletePetWrap(url='https://petstore.swagger.io/v2/pet')
class DeletePet:
    def __init__(self, pet):
        self.pet_id = pet
