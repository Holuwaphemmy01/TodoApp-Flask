from unittest import TestCase
from todo.services.register.register import register
from todo.dtos.request.registerRequest import RegisterRequest


class Test(TestCase):
    def test_that_user_cannot_register_when_firstname_is_empty(self):
        RegisterRequest.first_name = " "
        RegisterRequest.last_name = " "
        RegisterRequest.username = " "
        RegisterRequest.password = " "
        self.assertRaises(register(RegisterRequest))
