import requests
from data.user_data import UserData
import allure


class UserMethods:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/auth"

    allure.step("Регистрация пользователя")
    def register_user(self, user_data=None):
        data = user_data if user_data else UserData.generate_valid_user()
        response = requests.post(f"{self.BASE_URL}/register", json=data)
        return response.json()
    
    allure.step("Логин")
    def login_user(self, user_data):
        response = requests.post(f"{self.BASE_URL}/login", json=user_data)
        return response.json()
    
    allure.step("Обновить информацию о пользователе")
    def update_user(self, token, update_data):
        headers = {"Authorization": token}
        response = requests.patch(f"{self.BASE_URL}/user", headers=headers, json=update_data)
        return response.json()

    allure.step("Удалить пользователя")
    def delete_user(self, token):
        headers = {"Authorization": token}
        requests.delete(f"{self.BASE_URL}/user", headers=headers)
