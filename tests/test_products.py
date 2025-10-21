import unittest
from app.models import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Ном", 15000, "Програмчлалын ном")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Ном")
        self.assertEqual(self.product.price, 15000)
        self.assertEqual(self.product.description, "Програмчлалын ном")

    def test_product_price_validation(self):
        with self.assertRaises(ValueError):
            Product("Буруу бүтээгдэхүүн", -100, "Сөрөг үнэтэй")
