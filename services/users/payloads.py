from faker import Faker

fake = Faker("ru_RU")


class Payloads:
    valid_user = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }

    user_without_nickname = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }

    user_without_name = {
        "email": fake.email(),
        "password": fake.password(),
        "nickname": fake.user_name()
    }

    user_without_password = {
        "email": fake.email(),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }

    user_without_email = {
        "password": fake.password(),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }
