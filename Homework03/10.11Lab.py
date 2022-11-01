# Name: Sai Todupunoori
# PSID: 2048092

class FoodItem:

    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0, serving=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.serving = serving

    def get_calories(self, num_servings):
        calories = (self.fat * 9 + self.carbs * 4 + self.protein * 4) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(self.serving, self.get_calories(self.serving)))


if __name__ == '__main__':
    item_name = input()
    item_fat = float(input())
    item_carbs = float(input())
    item_protein = float(input())
    item_serving = float(input())
    f1 = FoodItem(serving=item_serving)
    f2 = FoodItem(item_name, item_fat, item_carbs, item_protein, item_serving)
    f1.print_info()
    print()
    f2.print_info()
