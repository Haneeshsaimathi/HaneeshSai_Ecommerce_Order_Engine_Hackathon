from product_service import products, product_locks

carts = {}

def add_to_cart(user, pid, qty):
    if pid not in products:
        print("Invalid product")
        return

    with product_locks[pid]:
        available = products[pid]["stock"] - products[pid]["reserved"]
        if qty > available:
            print("Not enough stock")
            return

        carts.setdefault(user, {})
        carts[user][pid] = carts[user].get(pid, 0) + qty
        products[pid]["reserved"] += qty
        print("Added to cart")

def remove_from_cart(user, pid):
    if user in carts and pid in carts[user]:
        qty = carts[user][pid]
        with product_locks[pid]:
            products[pid]["reserved"] -= qty
        del carts[user][pid]
        print("Removed")

def view_cart(user):
    print(carts.get(user, {}))
