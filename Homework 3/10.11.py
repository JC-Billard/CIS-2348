#JAKE BILLARD | UHID 1582534
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0, servings=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = servings
    def hm_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
    def pr_information(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    item1 = FoodItem()

    f_name = input()
    f_fat = float(input())
    f_carbs = float(input())
    f_protein = float(input())

    item2 = FoodItem(f_name, f_fat, f_carbs, f_protein)

    num_servings = float(input())

    item1.pr_information()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    item1.hm_calories(num_servings)))

    print()

    item2.pr_information()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    item2.hm_calories(num_servings)))
