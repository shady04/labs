import random

def get_random_password() -> str:

    a = "abcdefghjklmnopqrstuvwxyz"
    A = "ABCDEFGJKLMNOPQRSTUVWXYZ"
    num = '0123456789'
    b = a + A + num
    return random.sample(b, 8)




print(get_random_password())
