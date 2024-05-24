from faker import Faker
from django.contrib.auth import get_user_model

faker = Faker('es_ES')

class UserFactory:
    
    def build_user_json(self):
        return {
            "first_name":faker.first_name(), 
            "last_name":faker.last_name(),
            "username":faker.user_name(),
            "password":faker.password(), 
            "email":faker.email(), 
            #"image":faker.url() 
        }
    
    def create_user(self):
        return get_user_model().objects.create(**self.build_user_json())