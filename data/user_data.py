from helpers.helpers import GenerateData

class UserData:
    
    def generate_valid_user ():
        return GenerateData.generate_valid_user()

    def non_exist_account():
        return GenerateData.non_exist_account()
    
    missing_fields_users = [
        {"email": "", "password": "password", "name": "Name"},
        {"email": "test@mail.ru", "password": "", "name": "Name"},
        {"email": "test@mail.ru", "password": "password", "name": ""}
    ]

    existing_user_error = "User already exists"
    missing_fields_error = "Email, password and name are required fields"
    unauthorized_error = "You should be authorised"
    wrong_credentials_error = "email or password are incorrect"

