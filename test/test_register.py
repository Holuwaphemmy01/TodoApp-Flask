from unittest import TestCase
from todo.services.register.register import register
from todo.dtos.request.registerRequest import RegisterRequest


class Test(TestCase):
    register = register
    def test_that_user_cannot_register_when_firstname_is_empty(self):
        request = RegisterRequest
        request.set_first_name = 'r'
        request.lastName = ''
        # print(request)
        print(register(request))
        # self.assertRaises(register(request))




