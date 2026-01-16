import requests
import allure

class OrderMethods:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/orders"

    allure.step("Создание заказа")
    def create_order(self, ingredients, token=None):
        headers = {"Authorization": token} if token else {}
        response = requests.post(self.BASE_URL, headers=headers, json={"ingredients": ingredients})
        return response.json(), response.status_code

    allure.step("Получение заказа")
    def get_user_orders(self, token):
        headers = {"Authorization": token}
        response = requests.get(self.BASE_URL, headers=headers)
        return response.json(), response.status_code
    
    allure.step("Получение ингридиентов")
    def get_ingredients(self):
        url = "https://stellarburgers.nomoreparties.site/api/ingredients"
        response = requests.get(url)
        response.raise_for_status()
        ingredients = response.json().get('data', [])
        return [ingredient['_id'] for ingredient in ingredients]