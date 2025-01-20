from model.user import User, database
from dtos.request.registerRequest import RegisterRequest

def register(RegisterRequest: RegisterRequest):
    print(RegisterRequest)
    if  not RegisterRequest.__getattribute__(first_name).strip():
        raise ValueError("First name must be at least 2 characters long")
    if len(RegisterRequest.last_name) < 2:
        raise ValueError("Last name must be at least 2 characters long")
    if len(RegisterRequest.username) < 1:
         raise ValueError("Username cannot be empty")
    if len(RegisterRequest.password) < 6 or RegisterRequest.password.__contains__(" "):
        raise ValueError(
            "Password must be at least 6 characters long and cannot contain spaces"
        )


    User.last_name(RegisterRequest.last_name)
    User.first_name(RegisterRequest.first_name)
    User.username(RegisterRequest.username)
    User.password(RegisterRequest.password)

    database.session.add(User)
    database.session.commit()
    return User



