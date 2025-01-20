from model.user import User, database
from dtos.request.registerRequest import RegisterRequest

def register(register_request: RegisterRequest):
    if len(register_request.first_name) < 2:
        raise ValueError("First name must be at least 2 characters long")
    if len(register_request.last_name) < 2:
        raise ValueError("Last name must be at least 2 characters long")
    if len(register_request.username) < 2:
        raise ValueError("Username cannot be empty")
    if len(register_request.password) < 6 or " " in register_request.password:
        raise ValueError(
            "Password must be at least 6 characters long and cannot contain spaces"
        )


    user = User(
        first_name=register_request.first_name,
        last_name=register_request.last_name,
        username=register_request.username,
        password=register_request.password,
    )

    database.session.add(user)
    database.session.commit()

    return user

