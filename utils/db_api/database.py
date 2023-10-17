import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER,
                    full_name TEXT,
                    phone_number TEXT,
                    age INTEGER
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT,
                    price REAL,
                    description TEXT,
                    photo TEXT,
                    quantity INTEGER
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER,
                    order_id INTEGER,
                    status TEXT,
                    ordered_date TEXT,
                    total_product INTEGER,
                    total_price REAL,
                    latitude REAL NUL, 
                    longitude REAL NUL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   order_id INTEGER,
                   product_text TEXT,
                   price REAL,
                   quantity TEXT
            )
        """)
        self.conn.commit()

    def delete_table(self, table_name):
        self.cursor.execute(f"DROP TABLE {table_name}")
        self.conn.commit()

    def append_user(self, data):
        user_id = data.get("user_id")
        full_name = data.get("full_name")
        phone_number = data.get("phone_number")
        age = data.get("age")

        try:
            self.cursor.execute(f"""
                INSERT INTO users (telegram_id, full_name, phone_number, age)
                VALUES (?,?,?,?)
            """, (user_id, full_name, phone_number, age))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def get_user(self, message):
        return self.cursor.execute(f"SELECT * FROM users WHERE telegram_id={message.chat.id}").fetchone()

    def update_user_profile(self, message, column):
        try:
            new_value = message.text
            if column == "full_name":
                query = f"UPDATE users SET full_name = '{new_value}' WHERE telegram_id = {message.chat.id}"
                self.cursor.execute(query)

            elif column == "phone_number":
                query = f"UPDATE users SET phone_number = '{new_value}' WHERE telegram_id = {message.chat.id}"
                self.cursor.execute(query)

            elif column == "age":
                query = f"UPDATE users SET age = '{new_value}' WHERE telegram_id = {message.chat.id}"
                self.cursor.execute(query)

            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def append_product(self, data):
        product_name = data.get("product_name")
        price = data.get("price")
        description = data.get("description")
        photo = data.get("photo")
        quantity = data.get("quantity")

        try:
            self.cursor.execute(f"""
                INSERT INTO product (product_name, price, description, photo, quantity)
                VALUES (?,?,?,?,?)
            """, (product_name, price, description, photo, quantity))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def search_product_by_name(self, product_name):
        return self.cursor.execute(f"SELECT * FROM product WHERE product_name='{product_name}'").fetchone()

    def get_all_product(self):
        return self.cursor.execute(f"SELECT * FROM product").fetchall()

    def update_admin_sticker(self, sticker_id, column, new_value):
        try:
            query = f"UPDATE product SET {column} = '{new_value}' WHERE id = {sticker_id}"
            self.cursor.execute(query)

            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def delete_product(self, product_id):
        try:
            self.cursor.execute(f"DELETE FROM product WHERE id='{product_id}'")
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def append_item(self, products: list):
        self.cursor.executemany("INSERT INTO order_items (order_id, price, product_text, quantity) VALUES(?,?,?,?)",
                                products)
        self.conn.commit()

    def append_order(self, message, basket, order_id, longitude, latitude):
        products = list()

        total_product = 0
        total_price = 0
        for item in basket.values():
            temp_list = list()
            temp_list.append(order_id)
            temp_list.append(item['price'])
            temp_list.append(item['name'])
            temp_list.append(item['quantity'])
            products.append(tuple(temp_list))

            total_product += item['quantity']
            total_price += item['total']
        try:
            self.cursor.execute(f"""
                INSERT INTO orders (telegram_id, order_id, status, ordered_date, total_product, total_price, longitude, 
                latitude)
                VALUES (?,?,?,?,?,?,?,?)
            """, (message.chat.id, order_id, "Kutilmoqda", message.date, total_product, total_price, longitude,
                  latitude))
            self.append_item(products)

            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def append_order_t(self, message, basket, order_id):
        products = list()

        total_product = 0
        total_price = 0
        for item in basket.values():
            temp_list = list()
            temp_list.append(order_id)
            temp_list.append(item['price'])
            temp_list.append(item['name'])
            temp_list.append(item['quantity'])
            products.append(tuple(temp_list))

            total_product += item['quantity']
            total_price += item['total']
        try:
            self.cursor.execute(f"""
                INSERT INTO orders (telegram_id, order_id, status, ordered_date, total_product, total_price)
                VALUES (?,?,?,?,?,?)
            """, (message.chat.id, order_id, "Kutilmoqda", message.date, total_product, total_price))
            self.append_item(products)

            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def get_order_by_id(self, order_id):
        return self.cursor.execute(f"SELECT * FROM orders WHERE order_id={order_id}").fetchone()

    def get_all_orders_by_status(self, user_id, status):
        return self.cursor.execute(f"SELECT * FROM orders WHERE telegram_id={user_id} AND status='{status}'").fetchall()

    def get_user_by_id(self, user_id):
        return self.cursor.execute(f"SELECT * FROM users WHERE telegram_id={user_id}").fetchone()

    def get_all_orders_by_status_admin(self, status):
        return self.cursor.execute(f"SELECT * FROM orders WHERE status='{status}'").fetchall()

    def get_order_items_by_order_id(self, order_id):
        return self.cursor.execute(f"SELECT * FROM order_items WHERE order_id={order_id}").fetchall()

    def get_order_id(self, user_id):
        return self.cursor.execute(f"SELECT * FROM users WHERE telegram_id={user_id}").fetchone()

    def update_order_status(self, order_id, status_type):
        try:
            self.cursor.execute(f"""UPDATE orders SET status='{status_type}' WHERE order_id={order_id}""")
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False
