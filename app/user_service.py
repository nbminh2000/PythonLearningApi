from user_repository import UserRepository
from user import User


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, username, email):
        user = User(username=username, email=email)
        self.user_repository.add_user(user)
        return user

    def get_user(self, id):
        return self.user_repository.get_user_by_id(id)

    def get_all_users(self):
        return self.user_repository.get_all_users()
