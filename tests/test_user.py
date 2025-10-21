import unittest
from app.models import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("Бат", "бат@example.com")
        self.assertEqual(user.name, "Бат")
        self.assertEqual(user.email, "бат@example.com")

    def test_user_string_representation(self):
        user = User("Оюуна", "оюуна@example.com")
        self.assertEqual(str(user), "User Оюуна")
