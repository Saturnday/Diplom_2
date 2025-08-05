import allure
import pytest
from methods.user_methods import UserMethods
from data.user_data import UserData

@allure.feature("Регистрация")
class TestUserRegistration:

    @allure.title("Регистрация нового пользователя")
    def test_register_unique_user(self):
        response = UserMethods().register_user()
        assert response["success"] is True

    @allure.title("Регистрация существующего пользователя")
    def test_register_existing_user(self):
        user_methods = UserMethods()
        user = UserData.generate_valid_user()
        user_methods.register_user(user)
        response = user_methods.register_user(user)
        assert response["message"] == UserData.existing_user_error

    @allure.title("Регистрация без обязательных полей")
    @pytest.mark.parametrize("user_data", UserData.missing_fields_users)
    def test_register_missing_fields(self, user_data):
        response = UserMethods().register_user(user_data)
        assert response["message"] == UserData.missing_fields_error

