import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

@pytest.fixture
def new_user():
    user_data = UserMethods().register_user()
    yield user_data
    UserMethods().delete_user(user_data['accessToken'])

@pytest.fixture
def authorized_user(new_user):
    return new_user['accessToken']

@pytest.fixture(scope="session")
def valid_ingredients():
    return OrderMethods().get_ingredients()