# DATABASE_URL = "mysql+pymysql://root:Pravinth%40123@localhost/practice_pymysql"

# class A:
#     x = 'pravin'
#     _y = 'mahesh'
#     __z = 'raj'

#     def __init__(self, a) -> None:
#         self.a = a

#     def m(self):
#         # Properly accessing class-level variables
#         return self._A__z  # Private variable with name mangling

#     @classmethod
#     def m2(cls):
#         # Correctly creating an instance
#         instance = A(cls.x)  # Pass a valid argument
#         return instance.a  # Access the instance variable

# # Correct usage
# print(A("example").m())    # Accessing private variable __z
# print(A.m2())              # Class method works correctly




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Class method to instantiate the class
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         current_year = 2024
#         age = current_year - birth_year
#         return cls(name, age)  # Creates a new Person instance

# # Instantiate using the regular constructor
# p1 = Person("Alice", 30)

# # Instantiate using the class method
# p2 = Person.from_birth_year("Bob", 1990)

# print(f"{p1.name} is {p1.age} years old.")  # Output: Alice is 30 years old.
# print(f"{p2.name} is {p2.age} years old.")  # Output: Bob is 34 years old.


# class A:
#     def __init__(self,n) -> None:
#         print('from init')
#         self.n=n
#     @classmethod
#     def m1(cls,x):
#         return cls(x)
# print(A.m1(10))



# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     @classmethod
#     def from_dict(cls, data):
#         return cls(data["name"], data["position"])

# class Manager(Employee):
#     pass

# # Using class method with a subclass
# manager_data = {"name": "John", "position": "Manager"}
# manager = Manager.from_dict(manager_data)

# print(manager.name, manager.position)  # Output: John Manager





# class Shape:
#     def __init__(self, shape_type, dimensions):
#         self.shape_type = shape_type
#         self.dimensions = dimensions

#     @classmethod
#     def create_circle(cls, radius):
#         return cls("Circle", {"radius": radius})

#     @classmethod
#     def create_rectangle(cls, length, breadth):
#         return cls("Rectangle", {"length": length, "breadth": breadth})

# # Creating different shapes using class methods
# circle = Shape.create_circle(5)
# rectangle = Shape.create_rectangle(10, 20)

# print(circle.shape_type, circle.dimensions)    # Output: Circle {'radius': 5}
# print(rectangle.shape_type, rectangle.dimensions)  # Output: Rectangle {'length': 10, 'breadth': 20}




# class MyClass:
#     def __init__(self):
#         self._protected_var = "I am protected"

#     def _protected_method(self):
#         print("This is a protected method")

# class SubClass(MyClass):
#     def access_protected(self):
#         print(self._protected_var)  # Accessible in subclass
#         self._protected_method()    # Accessible in subclass

# obj = SubClass()
# obj.access_protected()
# print(obj._protected_var)  # Still accessible, but by convention should not be used

   
   
   
# class MyClass:
#     def __init__(self):
#         self.__private_var = "I am private"

#     def __private_method(self):
#         print("This is a private method")

#     def access_private(self):
#         print(self.__private_var)  # Accessible within the class
#         self.__private_method()    # Accessible within the class

# obj = MyClass()
# obj.access_private()

# # Trying to access private members directly will raise an AttributeError:
# # print(obj.__private_var)  # AttributeError
# # obj.__private_method()    # AttributeError

# # However, you can still access them using name mangling (not recommended):
# print(obj._MyClass__private_var)  # Works, but should be avoided





# Factory method

# from abc import ABC, abstractmethod

# class Notification(ABC):
#     @abstractmethod
#     def notify(self, message):
#         pass


# class SMSNotification(Notification):
#     def notify(self, message):
#         return f"Sending SMS: {message}"

# class EmailNotification(Notification):
#     def notify(self, message):
#         return f"Sending Email: {message}"

# class PushNotification(Notification):
#     def notify(self, message):
#         return f"Sending Push Notification: {message}"


# class NotificationFactory(ABC):
#     @abstractmethod
#     def create_notification(self):
#         pass

#     def send_notification(self, message):
#         # Factory Method is used here to create the notification
#         notification = self.create_notification()
#         return notification.notify(message)


# class SMSNotificationFactory(NotificationFactory):     # sms_factory = SMSNotificationFactory()
#     def create_notification(self):                     # sms_factory.send_notification("This is an SMS message.")
#         return SMSNotification()

# class EmailNotificationFactory(NotificationFactory):
#     def create_notification(self):
#         return EmailNotification()

# class PushNotificationFactory(NotificationFactory):
#     def create_notification(self):
#         return PushNotification()


# # Client Code
# sms_factory = SMSNotificationFactory()
# email_factory = EmailNotificationFactory()
# push_factory = PushNotificationFactory()

# print(sms_factory.send_notification("This is an SMS message."))  
# # Output: Sending SMS: This is an SMS message.

# print(email_factory.send_notification("This is an Email message."))  
# # Output: Sending Email: This is an Email message.

# print(push_factory.send_notification("This is a Push Notification message."))  
# # Output: Sending Push Notification: This is a Push Notification message.



# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             print(f"Creating a new instance {args[0]}")
#             cls._instance = super().__new__(cls)
#         else:
#             print(cls._instance)
#             print("Using existing instance")
#         return cls._instance

#     def __init__(self, value):
#         print('from init---------')
#         self.value = value

# # Create instances
# obj1 = Singleton(10)
# obj2 = Singleton(20)

# # print(obj1 is obj2)  # Output: True (Both are the same instance)
# # print(obj1.value)    # Output: 20 (Shared state)
# # print(obj2.value)    # Output: 20



# class A:
#     def __init__(self,x):
#         self.x=x
#     def m1(self,z):
#         return self.x+z
# class B(A):
#     def __init__(self,x,y):
#         self.y=y
#         super().__init__(x)
#         # A().__init__(x)
#     def m2(self,a):
#         # return self.x+ self.y
#         return self.m1(a)+ self.y
# b=B(5,6)
# print(b.m2(3))
    
    


