
class Meal:
    def __init__(self):
        self.item1 = 9.99
        self.item2 = 7.99
        self.item3 = 8.99
        self.item4 = 6.99
        self.item5 = 12.99

    def cost_of_meals(self, item1, item2, item3, item4, item5, total_meal_price):
        self.total_cost1 = round((item1 * self.item1) + (item2 * self.item1) + (item3 * self.item1) + (item4 * self.item1) + (item5 * self.item1), 2)
        total_meal_price.setText(f'${self.total_cost1}')

        return self.total_cost1

class Drink:
    def __init__(self):
        self.item1 = 4.99
        self.item2 = 5.99
        self.item3 = 3.99
        self.item4 = 3.99
        self.item5 = 1.99


    def cost_of_drinks(self, item1, item2, item3, item4, item5, total_drink_price):
        self.total_cost2 = round((item1 * self.item1) + (item2 * self.item1) + (item3 * self.item1) + (item4 * self.item1) + (item5 * self.item1), 2)
        total_drink_price.setText(f'${self.total_cost2}')

        return self.total_cost2

