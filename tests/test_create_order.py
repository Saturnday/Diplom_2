import allure
from methods.order_methods import OrderMethods
from data.order_data import OrderData

@allure.feature("Создать заказ")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией 200")
    def test_create_order_authorized(self, authorized_user, valid_ingredients):
        response, status = OrderMethods().create_order(valid_ingredients, authorized_user)
        assert status == 200
        assert response["success"] is True

    @allure.title("Создание заказа без авторизации 200")
    def test_create_order_unauthorized(self, valid_ingredients):
        response, status = OrderMethods().create_order(valid_ingredients)
        assert status == 200
        assert response["success"] is True

    @allure.title("Создание заказа без ингредиентов 400")
    def test_create_order_no_ingredients(self):
        response, status = OrderMethods().create_order([])
        assert status == 400
        assert response["message"] == OrderData.no_ingredients_error

    @allure.title("Создание заказа с неверными ингредиентами 400")
    def test_create_order_invalid_ingredients(self):
        response, status = OrderMethods().create_order(OrderData.invalid_ingredients)
        assert status == 400
