from .service import UsersService


class UsersRepository:
    def test(self):
        return UsersService().test()
