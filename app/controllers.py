from .models import Database


class ProductController:
    @staticmethod
    def get_all_products():
        return Database.get_all_products()

    @staticmethod
    def get_shopping_list():
        return Database.get_shopping_list()

    @staticmethod
    def add_product(name, quantity):
        if Database.product_exists(name):
            return False, "המוצר כבר קיים ברשימה"
        Database.add_product(name, quantity)
        return True, "המוצר נוסף בהצלחה"

    @staticmethod
    def search_products(query):
        return Database.search_products(query)

    @staticmethod
    def update_product(product_id, quantity):
        return Database.update_product(product_id, quantity)

    @staticmethod
    def delete_product(product_id):
        return Database.delete_product(product_id)

    @staticmethod
    def validate_product(name, quantity):
        if not name or len(name.strip()) == 0:
            return False, "שם המוצר לא יכול להיות ריק"
        try:
            quantity = int(quantity)
            if quantity < 0:
                return False, "הכמות חייבת להיות מספר חיובי"
        except ValueError:
            return False, "הכמות חייבת להיות מספר"
        return True, ""

