import sqlite3


class Database:
    @staticmethod
    def connect_db():
        return sqlite3.connect('inventory.db')

    @staticmethod
    def init_db():
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                quantity INTEGER NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS shopping_list (
                id INTEGER PRIMARY KEY,
                product_id INTEGER,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        ''')

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_products():
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('SELECT * FROM products')
        products = c.fetchall()
        conn.close()
        return products

    @staticmethod
    def get_shopping_list():
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute(
            'SELECT products.id, products.name FROM products JOIN shopping_list ON products.id = '
            'shopping_list.product_id')
        shopping_list = c.fetchall()
        conn.close()
        return shopping_list

    @staticmethod
    def add_product(name, quantity):
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def update_product(product_id, quantity):
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
        if quantity == 0:
            c.execute('INSERT INTO shopping_list (product_id) VALUES (?)', (product_id,))
        else:
            c.execute('DELETE FROM shopping_list WHERE product_id = ?', (product_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_product(product_id):
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('DELETE FROM products WHERE id = ?', (product_id,))
        c.execute('DELETE FROM shopping_list WHERE product_id = ?', (product_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def product_exists(name):
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('SELECT * FROM products WHERE name = ?', (name,))
        product = c.fetchone()
        conn.close()
        return product is not None

    @staticmethod
    def search_products(query):
        conn = Database.connect_db()
        c = conn.cursor()
        c.execute('SELECT * FROM products WHERE name LIKE ?', ('%' + query + '%',))
        products = c.fetchall()
        conn.close()
        return products
