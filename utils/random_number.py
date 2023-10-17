import random

from loader import db_manager


def get_random_id():
    try:
        random_num = random.randint(10000, 99999)
        order = db_manager.get_order_by_id(random_num)
        if order:
            if order[3] == "DELIVERED" or order[3] == "CANCELED":
                return random_num
            else:
                get_random_id()
        return random_num
    except Exception as exc:
        print(exc)
        return 00000
