# from model.user import User, database
# from dtos.request.registerRequest import RegisterRequest
#
# def register(RegisterRequest: RegisterRequest):
#     print(RegisterRequest)
#     if  RegisterRequest..strip():
#         raise ValueError("First name must be at least 2 characters long")
#     if len(RegisterRequest.last_name) < 2:
#         raise ValueError("Last name must be at least 2 characters long")
#     if len(RegisterRequest.username) < 1:
#          raise ValueError("Username cannot be empty")
#     if len(RegisterRequest.password) < 6 or RegisterRequest.password.__contains__(" "):
#         raise ValueError(
#             "Password must be at least 6 characters long and cannot contain spaces"
#         )
#
#
#     User.last_name(RegisterRequest.last_name)
#     User.first_name(RegisterRequest.first_name)
#     User.username(RegisterRequest.username)
#     User.password(RegisterRequest.password)
#
#     database.session.add(User)
#     database.session.commit()
#     return User
#
#
#


from model.user import User, database
from dtos.request.registerRequest import RegisterRequest

def register(register_request: RegisterRequest):
    print(register_request)

    if len(register_request.first_name.strip()) < 2:
        raise ValueError("First name must be at least 2 characters long")
    if len(register_request.last_name) < 2:
        raise ValueError("Last name must be at least 2 characters long")
    if len(register_request.username) < 1:
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

