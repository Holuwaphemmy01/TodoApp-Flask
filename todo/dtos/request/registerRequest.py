class RegisterRequest:
     def __init__(self, username, password, first_name, last_name):
         self.__username = username
         self.__password = password
         self.__first_name = first_name
         self.__last_name = last_name


     @property
     def password(self):
        return self.__password

     @password.setter
     def set_password(self, value):
         self.__password = value


     @property
     def first_name(self):
        return self.__first_name

     @first_name.setter
     def set_first_name(self, value):
        self.__first_name = value

     @property
     def last_name(self):
         return self.__last_name

     @last_name.setter
     def set_last_name(self, value):
         self.__last_name = value

     @property
     def username(self):
        return self.__username

     @username.setter
     def username(self, value):
        self.__username = value


