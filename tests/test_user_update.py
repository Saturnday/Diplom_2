import allure
from methods.user_methods import UserMethods
from data.user_data import UserData

@allure.feature("Логин")
class TestUserLogin:

    @allure.title("Успешный логин пользователя")
    def test_successful_login(self, new_user):
        response = UserMethods().login_user({
            "email": new_user["user"]["email"],
            "password": "password123"
        })
        assert response["user"]["email"] == new_user["user"]["email"]

    @allure.title("Логин с несуществующими данными")
    def test_login_wrong_credentials(self):
        response = UserMethods().login_user(UserData.non_exist_account())
        assert response["message"] == UserData.wrong_credentials_error
