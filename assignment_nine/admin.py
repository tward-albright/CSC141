from .user import User


class Privleges:
    def __init__(self, privleges):
        self.privleges = privleges

    def show_privleges(self):
        print("This user can:")
        for priv in self.privleges:
            print(f"  {priv}")


class Admin(User):
    def __init__(self, first, last, user, bday, privleges):
        super().__init__(first, last, user, bday)
        self.privleges = privleges
