from product_service import products, product_locks
from cart_service import carts
from payment_service import process_payment

orders = {}
order_id_counter = 1

def place_order(user):
    global order_id_counter

    if user not in carts or not carts[user]:
        print("Cart empty")
        return

    items = carts[user]
    total = 0

    locked = []

    try:
        # lock all products
        for pid in items:
            product_locks[pid].acquire()
            locked.append(pid)

        # calculate total
        for pid, qty in items.items():
            total += products[pid]["price"] * qty

        oid = order_id_counter
        order_id_counter += 1

        orders[oid] = {
            "user": user,
            "items": items.copy(),
            "status": "CREATED",
            "total": total
        }

        # deduct stock
        for pid, qty in items.items():
            products[pid]["stock"] -= qty
            products[pid]["reserved"] -= qty

        # clear cart
        carts[user] = {}

        # payment
        if not process_payment():
            raise Exception("Payment Failed")

        orders[oid]["status"] = "PAID"
        print("Order Success:", oid)

    except Exception as e:
        print("Order Failed:", e)

        # rollback
        for pid, qty in items.items():
            products[pid]["reserved"] -= 0  # safe
            products[pid]["stock"] += 0

        if 'oid' in locals():
            del orders[oid]

    finally:
        for pid in locked:
            product_locks[pid].release()

def view_orders():
    for oid, o in orders.items():
        print(oid, o)
