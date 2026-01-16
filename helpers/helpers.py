import random

class GenerateData:
    def random_email():
        return f"test{random.randint(1000,9999)}@mail.ru"
        
    @staticmethod
    def generate_valid_user():
        return {
            "email": f"test{random.randint(1000, 9999)}@mail.ru",
            "password": "password123",
            "name": "TestUser"
        }
    
    @staticmethod
    def non_exist_account():
        return {
            "email": f"nonexist{random.randint(1000, 9999)}@mail.ru",
            "password": "wrongpassword"
        }
