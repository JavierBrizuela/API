from rest_framework.test import APITestCase
from rest_framework import status
from .factory.user import UserFactory

class TestSetUp(APITestCase):
    
    def setUp(self):
        
        self.signup_url = '/api/singup/'
        self.user = UserFactory().build_user_json()
        print(self.user)
        response = self.client.post(
            self.signup_url,
            self.user,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.login_url = '/api/login/'
        response = self.client.post(
            self.login_url,
            {
                "email":self.user['email'],
                "password":self.user["password"]
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.refresh = response.data['refresh']
        
        return super().setUp()