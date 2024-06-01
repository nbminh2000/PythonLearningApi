from user import db, User

class UserRepository:
    def add_user(self, user):
        db.session.add(user)
        db.session.commit()

    def get_user_by_id(self, id):
        return User.query.get(id)

    def get_all_users(self):
        return User.query.all()
