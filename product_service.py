from threading import Lock

products = {}
product_locks = {}

def add_product(pid, name, price, stock):
    if pid in products:
        print("Product ID already exists")
        return
    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "reserved": 0
    }
    product_locks[pid] = Lock()

def view_products():
    for pid, p in products.items():
        print(pid, p)
