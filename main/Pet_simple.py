import requests
import json


class Pet:

    def __init__(self, pet_id, categ_name="", pet_name="", status="available", tag_name="", photo_url=""):
        self.url = 'https://petstore.swagger.io/v2/pet/'
        self.api_key = 'special-key'
        self.pet_id = pet_id
        self.categ_name = categ_name
        self.pet_name = pet_name
        self.status = status
        self.tag_name = tag_name
        self.photo_url = photo_url

        self.payload = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": categ_name
            },
            "name": pet_name,
            "photoUrls": [photo_url],
            "tags": [
                {
                    "id": 0,
                    "name": tag_name
                }
            ],
            "status": status
        }
        self.header = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'api-key': self.api_key
        }

    def get_pet(self):
        """ Requests a pet by id, returns response code
        """
        url_loc = self.url + str(self.pet_id)
        r = requests.get(url_loc)
        return r.status_code

    def create_pet(self):
        r = requests.post(self.url, data=json.dumps(self.payload), headers=self.header)
        return self.payload == r.json()

    def update_pet(self, categ_name="", pet_name="", status="available", tag_name="", photo_url=""):
        """ Updates the pet with id name and returns True.
        """

        self.url = 'https://petstore.swagger.io/v2/pet/'
        self.categ_name = categ_name
        self.pet_name = pet_name
        self.status = status
        self.tag_name = tag_name
        self.photo_url = photo_url

        self.payload = {
            "id": self.pet_id,
            "category": {
                "id": 0,
                "name": categ_name
            },
            "name": pet_name,
            "photoUrls": [photo_url],
            "tags": [
                {
                    "id": 0,
                    "name": tag_name
                }
            ],
            "status": status
        }
        self.header = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'api-key': self.api_key
        }

        r = requests.put(self.url, data=json.dumps(self.payload), headers=self.header)

        # verify that the pet was updated
        js = r.json()
        return self.payload == js

    def delete_pet(self):
        """ Deletes a pet by id, returns status code
        """
        url_loc = self.url + str(self.pet_id)
        r = requests.delete(url_loc, data=json.dumps(self.payload), headers=self.header)
        return r.status_code

    def print_pet(self):
        """ Requests a pet by id and prints out its response
        """
        url_loc = self.url + str(self.pet_id)
        r = requests.get(url_loc)
        r_text = json.dumps(r.text, sort_keys=True, indent=4)
        print(f"response code is: {r.status_code}")
        print(f"response is:      {r_text}")



