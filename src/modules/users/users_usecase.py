from datetime import datetime, timedelta, timezone
import os
from src.modules.users.users_viewmodel import UsersViewModel
from src.shared.entities.user import User
from src.modules.users.users_repository import UsersRepository
import bcrypt
import jwt

class UsersUseCase:
    def __init__(self, repo: UsersRepository):
        self.repo = repo
        self.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

    def create(self, data: dict):
        if not data["email"] or not data["name"] or not data["phone"] or not data["password"]:
            raise Exception("Campos obrigatórios não preenchidos")
            
        password = data["password"]
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        
        try:
            user = User(
                admin=False,
                email=data["email"],
                name=data["name"],
                phone=data["phone"],
                password_hash=hashed_password,
                restaurant=data["restaurant"],
                image=data["image"],
            )
            self.repo.create(user=user.model_dump())

            viewmodel = UsersViewModel(
                admin=user.admin,
                email=user.email,
                name=user.name,
                phone=user.phone,
                password_hash=hashed_password,
                restaurant=user.restaurant,
                created_at=user.created_at,
                updated_at=user.updated_at
            )

            return viewmodel.model_dump_json()
        except Exception as e:
            raise e

    def get_by_email(self, email):
        user = self.repo.get_by_email(email)
        if not user:
            raise Exception("Usuário não encontrado")
        return user

    def login(self, email: str, password: str):
        user = self.repo.get_user_to_login(email)
        if not user:
            raise Exception("Usuário não encontrado")
        
        if not bcrypt.checkpw(password.encode("utf-8"), user["password_hash"]):
            raise Exception("Senha incorreta")
        
        payload = {
            "sub": str(id(user)),
            "phone": user["phone"],
            "name": user["name"],
            "email": user["email"],
            "restaurant": user["restaurant"],
            "exp": datetime.now(timezone.utc) + timedelta(minutes=1440)
        }
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return {"token": token}
