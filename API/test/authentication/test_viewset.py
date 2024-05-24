from test.test_setup import TestSetUp
from rest_framework import status
from test.factory.user import UserFactory

class AuthenticationTestCase(TestSetUp):
    
    def test_profile_user(self):
        
        self.profile_url = '/api/perfil/'
        response = self.client.get(
            self.profile_url,
            format='json',
            HTTP_AUTHORIZATION = 'Bearer ' + self.token
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user['email'])
        
        user_update = UserFactory().build_user_json()
        response = self.client.patch(
            self.profile_url,
            user_update,
            format='json',            
            HTTP_AUTHORIZATION = 'Bearer ' + self.token
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_change_password(self):
        
        self.profile_url = '/api/change-password/'
        response = self.client.put(
            self.profile_url,
            {
                'password': self.user['password'],
                'new_password': "stringst",
                'confirm_password': "stringst"
                },
            format='json',
            HTTP_AUTHORIZATION = 'Bearer ' + self.token
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response = self.client.put(
            self.profile_url,
            {
                'password': self.user['password'],
                'new_password': "stringst",
                'confirm_password': "stringst123"
                },
            format='json',
            HTTP_AUTHORIZATION = 'Bearer ' + self.token
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        response = self.client.put(
            self.profile_url,
            {
                'password': 'wrongPassword',
                'new_password': "stringst",
                'confirm_password': "stringst"
                },
            format='json',
            HTTP_AUTHORIZATION = 'Bearer ' + self.token
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)