import unittest
from app import create_app
from app.models import Database


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        Database.init_db()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        response = self.client.post('/add_product', data=dict(
            name='test product',
            quantity='5'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        products = Database.get_all_products()
        self.assertTrue(any(product[1] == 'test product' for product in products))

    def test_update_product(self):
        # Add a product first
        self.client.post('/add_product', data=dict(name='update test', quantity='10'))
        products = Database.get_all_products()
        product_id = next(product[0] for product in products if product[1] == 'update test')

        response = self.client.post('/update_product', data=dict(
            product_id=product_id,
            quantity='15'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        updated_products = Database.get_all_products()
        updated_product = next(product for product in updated_products if product[0] == product_id)
        self.assertEqual(updated_product[2], 15)

    def test_delete_product(self):
        # Add a product first
        self.client.post('/add_product', data=dict(name='delete test', quantity='5'))
        products = Database.get_all_products()
        product_id = next(product[0] for product in products if product[1] == 'delete test')

        response = self.client.get(f'/delete_product/{product_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        updated_products = Database.get_all_products()
        self.assertFalse(any(product[0] == product_id for product in updated_products))

    def test_low_stock_products(self):
        # Add products with different quantities
        self.client.post('/add_product', data=dict(name='low stock 1', quantity='1'))
        self.client.post('/add_product', data=dict(name='low stock 2', quantity='2'))
        self.client.post('/add_product', data=dict(name='normal stock', quantity='5'))

        low_stock = Database.get_low_stock_products()
        self.assertEqual(len(low_stock), 2)
        self.assertTrue(any(product[1] == 'low stock 1' for product in low_stock))
        self.assertTrue(any(product[1] == 'low stock 2' for product in low_stock))
        self.assertFalse(any(product[1] == 'normal stock' for product in low_stock))

    def test_shopping_list(self):
        # Add a product with zero quantity
        self.client.post('/add_product', data=dict(name='shopping list test', quantity='0'))

        shopping_list = Database.get_shopping_list()
        self.assertEqual(len(shopping_list), 1)
        self.assertEqual(shopping_list[0][1], 'shopping list test')

    def test_invalid_product_name(self):
        response = self.client.post('/add_product', data=dict(
            name='',
            quantity='5'
        ), follow_redirects=True)
        self.assertIn('שם המוצר לא יכול להיות ריק', response.data.decode('utf-8'))

    def test_invalid_product_quantity(self):
        response = self.client.post('/add_product', data=dict(
            name='invalid quantity test',
            quantity='-5'
        ), follow_redirects=True)
        self.assertIn('הכמות חייבת להיות מספר חיובי', response.data.decode('utf-8'))

    def tearDown(self):
        # Clear the database after each test
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('DELETE FROM products')
        c.execute('DELETE FROM shopping_list')
        conn.commit()
        conn.close()

    if __name__ == '__main__':
        unittest.main()