
class ReceiptPrint:
    def __init__(self):
        self.item_list = '\n	      Food Management System            \n'

    def item_load(self, items_bought, label, tax, subtotal, total, date):
        for name, item in items_bought.items():
            if item >= 1:
                self.item_list += f'\n   *  {name}{5 * " "}{item}\n'

        self.item_list += '\n=========================================\n'
        self.item_list += f'\n   *  Tax:{5 * " "}${tax}\n'
        self.item_list += f'\n   *  Subtotal:{5 * " "}${subtotal}\n'
        self.item_list += f'\n   *  Total:{5 * " "}${total}\n'
        self.item_list += '\n=========================================\n'
        self.item_list += f'  Date: {date}'

        label.setPlainText(f'{self.item_list}')

