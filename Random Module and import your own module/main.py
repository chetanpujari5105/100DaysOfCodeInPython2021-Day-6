import random
import my_module
rand_int = random.randint(1,10)
print(rand_int)

print(my_module.pi)
rand_float = random.random() * 5 # from 0.00000... to 4.99999999...
print(rand_float)

love_score = random.randint(0,100)
print(f"Your love score is {love_score}")