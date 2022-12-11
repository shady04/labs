import random
def get_unique_list_numbers() -> list[int]:

    while True:
        a = [random.randint(-10,10) for _ in range(15)]
        if len(a) == len(set(a)):
            return a
        else:
            continue


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
