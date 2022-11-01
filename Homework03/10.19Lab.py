# Name: Sai Todupunoori
# PSID: 2048092

class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))

    def print_item_cost(self):
        total = self.item_price * self.item_quantity

        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total))


class ShoppingCart:

    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):
        cond = False
        for x in self.cart_items:
            if x.item_name == itemName:
                self.cart_items.remove(x)
                cond = True
                break
        print('Item not found in cart. Nothing removed.') if not cond else None
        print("")

    def modify_item(self, itemToPurchase):
        cond = False
        list_len = len(self.cart_items)
        for i in range(list_len):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                cond = True
                self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                break
        print('Item not found in cart. Nothing modified.') if not cond else None
        print("")

    def get_num_items_in_cart(self):
        items = 0
        for i in self.cart_items: items = items + i.item_quantity
        return items

    def get_cost_of_cart(self):
        total_cost = 0
        items = 0
        for i in self.cart_items: total_cost += (i.item_quantity * i.item_price)
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print('\nTotal: {}'.format(total_cost))
            print()

    def print_descriptions(self):
        quantity = len(self.cart_items)
        if quantity == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items: item.print_item_description()

    # sds
    def output_shopping(self):
        print("OUTPUT SHOPPING CART")
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:', self.get_num_items_in_cart(), end='\n\n')
        total = 0
        quantity = len(self.cart_items)
        if quantity == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                item.print_item_cost()
                total += (item.item_quantity * item.item_price)
        print('\nTotal: ${}'.format(total), end='\n')
        print("")


def print_menu(c_cart):
    customer_Cart = c_cart
    select = ''
    while select != 'q':
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("")

        select = input('Choose an option:\n')
        while select != 'a' and select != 'o' and select != 'i' and select != 'q' and select != 'r' and select != 'c':
            select = input('Choose an option:\n')
        if select == 'a':
            print("ADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            print("")
            itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(itemtoPurchase)

        elif select == 'o':
            customer_Cart.output_shopping()
        elif select == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            customer_Cart.print_descriptions()
            print("")
        elif select == 'r':
            print('REMOVE ITEM FROM CART')
            itemName = input('Enter name of item to remove:\n')
            customer_Cart.remove_item(itemName)
        elif select == 'c':
            print('CHANGE ITEM QUANTITY')
            name = input('Enter the item name:\n')
            quantity = int(input('Enter the new quantity:\n'))
            itemToPurchase = ItemToPurchase(name, 0, quantity)
            customer_Cart.modify_item(itemToPurchase)
        # elif select == "q":
        #     break


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name: {}".format(customer_name))
    print("Today's date: {}".format(current_date))
    print("")
    c_cart = ShoppingCart(customer_name, current_date)
    print_menu(c_cart)
