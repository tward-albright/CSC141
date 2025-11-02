class User:
    def __init__(self, first_name, last_name, username, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birthday = birthday
        self.login_attempts = 0

    def describe_user(self):
        print(f"""{self.username}:
                    First name: {self.first_name}
                    Last name: {self.last_name}
                    Birthday: {self.birthday}
            """)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
