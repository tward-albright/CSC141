def long_enough(password: str) -> bool:
    return len(password) >= 15


def special_character(password: str) -> bool:
    for char in password:
        if char in "?!@#$%^&*-_":
            return True
    return False


def has_number(password: str) -> bool:
    for char in password:
        if char.isdigit():
            return True
    return False


def has_lower(password: str) -> bool:
    for char in password:
        if char.islower():
            return True
    return False

def has_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


# at least 15 chars
# 1+ special character
# 1+ number
# 1+ capital letter
# 1+ lowercase letter
def password_check(password: str):
    return (
        long_enough(password)
        and special_character(password)
        and has_number(password)
        and has_lower(password)
        and has_upper(password)
    )


def main():
    print(
        "Enter a 15 character password, with one special character, one number, one capital letter, one lowercase"
    )
    user_pass = input()
    if password_check(user_pass):
        print("Password accepted!")
    else:
        print("Password rejected.")


main()
