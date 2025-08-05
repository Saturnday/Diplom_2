import allure
from methods.order_methods import OrderMethods
from data.order_data import OrderData

@allure.feature("Получить заказ")
class TestGetUserOrders:

    @allure.title("Получение заказов с авторизацией 200")
    def test_get_orders_authorized(self, authorized_user):
        response, status = OrderMethods().get_user_orders(authorized_user)
        assert status == 200
        assert response["success"] is True

    @allure.title("Получение заказов без авторизации 401")
    def test_get_orders_unauthorized(self):
        response, status = OrderMethods().get_user_orders("")
        assert status == 401
        assert response["message"] == OrderData.unauthorized_error
