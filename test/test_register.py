import unittest
from flask import Flask
from todo.services.register.register import register
from todo.dtos.request.registerRequest import RegisterRequest
from model.user import User, database

class TestUserRegistration(unittest.TestCase):

    def test_user_cannot_register_when_firstname_is_empty(self):
        request = RegisterRequest()
        request.set_first_name = ""
        request.set_last_name = " "
        request.set_username = "johndoe"
        request.set_password = "password123"
        with self.assertRaises(ValueError):
            register(request)

    def test_user_cannot_register_when_lastname_is_empty(self):
        request = RegisterRequest()
        request.set_first_name = "John"
        request.set_last_name = " "
        request.set_username = "johndoe"
        request.set_password = "password123"
        with self.assertRaises(ValueError):
            register(request)

    def test_user_cannot_register_when_username_is_empty(self):
        request = RegisterRequest()
        request.set_first_name = "John"
        request.set_last_name = "Doe"
        request.set_username = " "
        request.set_password = "password123"
        with self.assertRaises(ValueError):
            register(request)

    def test_user_cannot_register_when_password_is_empty(self):
        request = RegisterRequest()
        request.set_first_name = "John"
        request.set_last_name = "Doe"
        request.set_username = "johndoe"
        request.set_password = " "
        with self.assertRaises(ValueError):
            register(request)

    def test_user_cannot_register_when_password_is_less_than_8(self):
        request = RegisterRequest()
        request.set_first_name = "John"
        request.set_last_name = "Doe"
        request.set_username = "johndoe"
        request.set_password = "passw"
        with self.assertRaises(ValueError):
            register(request)

    def test_that_user_cannot_register_when_username_contains_space(self):
        request = RegisterRequest()
        request.set_first_name = "John"
        request.set_last_name = "Doe"
        request.set_username = "johndoe"
        request.set_password = "passw ord "
        with self.assertRaises(ValueError):
            register(request)

    def test_user_can_register_successfully(self):
        request = RegisterRequest()
        request.set_first_name = "John"
        request.set_last_name = "Doe"
        request.set_username = "johndoe"
        request.set_password = "password123"
        user = register(request)
        self.assertEqual(user.first_name, "John")


