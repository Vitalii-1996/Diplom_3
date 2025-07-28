import random
import string
import data
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('generate random email')
def generate_random_email():
    return f'{generate_random_string(8)}@{generate_random_string(4)}.{generate_random_string(3)}'

@allure.step('get random bun index')
def random_bun_index():
    return random.randint(0,data.BUN_COUNT-1)

@allure.step('get random igredient index')
def random_ingerdient_index():
    return random.randint(data.BUN_COUNT,data.INGREDIENT_COUNT)