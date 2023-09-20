"""Unittest of store.py"""
import unittest
from store import Store, StoreExceptions
from products import Product


class TestStore(unittest.TestCase):
    """Test Store"""

    def setUp(self):  # Ilginc doc string istemiyor
        # setUp store to Store class
        # All store attributes are Store instance
        self.product1 = Product("Test Product 1", 10.0, 100)
        self.product2 = Product("Test Product 2", 15.0, 50)
        self.store = Store([self.product1, self.product2])
        # print(type(self.store))
        # print(self.store.stock[0])

    def test_add_product(self):
        """Test creating a new Product and checking 
        if new product can be appended to the Store list"""
        new_product = Product("New Product", 20.0, 200)
        self.store.add_product(new_product)  # Store class method
        self.assertIn(new_product, self.store.stock)  # Test Store method

    def test_remove_product(self):
        """Test to remove and check it if really removed"""
        self.store.remove_product(self.product1)
        self.assertNotIn(self.product1, self.store.stock)

        # Test removing a product that doesn't exist
        non_existent_product = Product("Non-existent Product", 5.0, 10)
        with self.assertRaises(StoreExceptions):
            self.store.remove_product(non_existent_product)

    def test_get_total_quantity(self):
        """Test it item has same quantity after removed product"""
        self.assertEqual(self.store.get_total_quantity(), 150)

    def test_get_all_products(self):
        """Test"""
        self.assertEqual(len(self.store.get_all_products()), 2)

        # Deactivate a product and check if it's not in the list
        self.product1.deactivate()
        self.assertEqual(len(self.store.get_all_products()), 1)

    def active_products(self):
        """Deactive yapilan bir nesnenin get_all_products ile kontrol edilmesi"""
        product1 = Product("Test Product 1", 10.0, 100)
        product2 = Product("Test Product 2", 15.0, 50)
        self.store = Store([product1, product2])
        product1.deactivate()
        active_products = self.store.get_all_products()
        print(len(active_products))

    def test_str(self):
        """Bu ne"""
        store_string = str(self.store)
        self.assertIn("Test Product 1", store_string)
        self.assertIn("Test Product 2", store_string)


if __name__ == '__main__':
    # unittest.main()
    depo = TestStore()
    depo.active_products()
