import random

def random_email():
    return f"test{random.randint(1000,9999)}@mail.ru"

class UserData:
    
    @staticmethod
    def generate_valid_user():
        return {
            "email": f"test{random.randint(1000, 9999)}@mail.ru",
            "password": "password123",
            "name": "TestUser"
        }


    missing_fields_users = [
        {"email": "", "password": "password", "name": "Name"},
        {"email": "test@mail.ru", "password": "", "name": "Name"},
        {"email": "test@mail.ru", "password": "password", "name": ""}
    ]

    existing_user_error = "User already exists"
    missing_fields_error = "Email, password and name are required fields"
    unauthorized_error = "You should be authorised"
    wrong_credentials_error = "email or password are incorrect"

    @staticmethod
    def non_exist_account():
        return {
            "email": f"nonexist{random.randint(1000, 9999)}@mail.ru",
            "password": "wrongpassword"
        }