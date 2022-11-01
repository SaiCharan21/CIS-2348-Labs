# Name: Sai Todupunoori
# PSID: 2048092

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total_price))


if __name__ == '__main__':
    print('Item 1')
    print('Enter the item name:')
    n1 = input()
    print('Enter the item price:')
    pr1 = int(input())
    print('Enter the item quantity:')
    q1 = int(input())

    print()

    print('Item 2')
    print('Enter the item name:')
    n2 = input()
    print('Enter the item price:')
    pr2 = int(input())
    print('Enter the item quantity:')
    q2 = int(input())

    print()
    i1 = ItemToPurchase(n1, pr1, q1)
    i2 = ItemToPurchase(n2, pr2, q2)
    print('TOTAL COST')
    i1.print_item_cost()
    i2.print_item_cost()
    print('\nTotal: ${}'.format((q1 * pr1) + q2 * pr2))
