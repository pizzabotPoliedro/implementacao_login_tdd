import pytest
import bcrypt
from datetime import datetime
from src.modules.users.users_usecase import UsersUseCase
from src.shared.entities.user import User

class MockUsersRepository:
    def __init__(self):
        self.users = {}
        self.secret_key = "test_secret_key"
    
    def create(self, user):
        if user["email"] in self.users:
            raise Exception("Email já existe")
        self.users[user["email"]] = user
        return True
    
    def get_user_to_login(self, email):
        if email not in self.users:
            return None
        return self.users[email]
    
    def get_by_email(self, email):
        if email not in self.users:
            return None
        return self.users[email]

class TestUsersUseCase:
    
    @pytest.fixture
    def users_usecase(self):
        repo = MockUsersRepository()
        return UsersUseCase(repo)
    
    @pytest.fixture
    def valid_user_data(self):
        return {
            "email": "test@example.com",
            "name": "Test User",
            "phone": "123456789",
            "password": "password123",
            "restaurant": False,
            "image": None
        }
    
    def test_create_user_with_valid_data(self, users_usecase, valid_user_data):
        result = users_usecase.create(valid_user_data)
        assert result is not None
        
        user = users_usecase.repo.get_by_email(valid_user_data["email"])
        assert user is not None
        assert user["email"] == valid_user_data["email"]
        assert user["name"] == valid_user_data["name"]
        assert user["phone"] == valid_user_data["phone"]
        assert bcrypt.checkpw(valid_user_data["password"].encode("utf-8"), user["password_hash"])
    
    def test_create_user_with_existing_email(self, users_usecase, valid_user_data):
        users_usecase.create(valid_user_data)
        
        with pytest.raises(Exception) as excinfo:
            users_usecase.create(valid_user_data)
        
        assert "Email já existe" in str(excinfo.value)
    
    def test_login_with_valid_credentials(self, users_usecase, valid_user_data):
        users_usecase.create(valid_user_data)
        
        result = users_usecase.login(valid_user_data["email"], valid_user_data["password"])
        
        assert "token" in result
        assert result["token"] is not None
    
    def test_login_with_invalid_email(self, users_usecase, valid_user_data):
        users_usecase.create(valid_user_data)
        
        with pytest.raises(Exception) as excinfo:
            users_usecase.login("wrong@example.com", valid_user_data["password"])
        
        assert "Usuário não encontrado" in str(excinfo.value)
    
    def test_login_with_invalid_password(self, users_usecase, valid_user_data):
        users_usecase.create(valid_user_data)
        
        with pytest.raises(Exception) as excinfo:
            users_usecase.login(valid_user_data["email"], "wrong_password")
        
        assert "Senha incorreta" in str(excinfo.value)
    
    def test_required_fields_validation(self, users_usecase):
        invalid_data = {
            "email": "",
            "name": "Test User",
            "phone": "123456789",
            "password": "password123",
            "restaurant": False,
            "image": None
        }
        
        with pytest.raises(Exception):
            users_usecase.create(invalid_data)
        
        invalid_data = {
            "email": "test@example.com",
            "name": "",
            "phone": "123456789",
            "password": "password123",
            "restaurant": False,
            "image": None
        }
        
        with pytest.raises(Exception):
            users_usecase.create(invalid_data)
        
        invalid_data = {
            "email": "test@example.com",
            "name": "Test User",
            "phone": "",
            "password": "password123",
            "restaurant": False,
            "image": None
        }
        
        with pytest.raises(Exception):
            users_usecase.create(invalid_data)
        
        invalid_data = {
            "email": "test@example.com",
            "name": "Test User",
            "phone": "123456789",
            "password": "",
            "restaurant": False,
            "image": None
        }
        
        with pytest.raises(Exception):
            users_usecase.create(invalid_data)
