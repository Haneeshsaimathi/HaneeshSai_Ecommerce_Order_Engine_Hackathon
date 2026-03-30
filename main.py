from product_service import *
from cart_service import *
from order_service import *
from logger import *
import threading

def simulate_concurrent():
    t1 = threading.Thread(target=add_to_cart, args=("A", 1, 5))
    t2 = threading.Thread(target=add_to_cart, args=("B", 1, 5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def menu():
    while True:
        print("\n1 Add Product\n2 View Products\n3 Add to Cart\n4 Remove\n5 View Cart\n6 Place Order\n7 View Orders\n8 Logs\n9 Concurrency Test\n0 Exit")
        ch = int(input())

        if ch == 1:
            pid = int(input("ID: "))
            name = input("Name: ")
            price = int(input("Price: "))
            stock = int(input("Stock: "))
            add_product(pid, name, price, stock)

        elif ch == 2:
            view_products()

        elif ch == 3:
            user = input("User: ")
            pid = int(input("Product ID: "))
            qty = int(input("Qty: "))
            add_to_cart(user, pid, qty)

        elif ch == 4:
            user = input("User: ")
            pid = int(input("Product ID: "))
            remove_from_cart(user, pid)

        elif ch == 5:
            user = input("User: ")
            view_cart(user)

        elif ch == 6:
            user = input("User: ")
            place_order(user)

        elif ch == 7:
            view_orders()

        elif ch == 8:
            view_logs()

        elif ch == 9:
            simulate_concurrent()

        elif ch == 0:
            break

menu()
