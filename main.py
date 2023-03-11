
def f(x):
    return 1 # your f(x) here

def f_prime(x):
    return 1 # your f'(x) here

x = 1 # starting point

for i in range(15):
    print(f"Step: {i} = {x}")
    x = x - f(x) / f_prime(x)

# output:
# f(x) = x ** 3 - 5 * x ** 2 + 8 * x - 5
# f'(x) = 3 * x ** 2 - 10 * x + 8
# starting from 2.5
# Step: 0 = 2.5
# Step: 1 = 2.857142857142857
# Step: 2 = 2.7641369047619038
# Step: 3 = 2.7549634823950333
# Step: 4 = 2.7548776737139558
# Step: 5 = 2.754877666246692
# Step: 6 = 2.7548776662466943
# Step: 7 = 2.754877666246692
# Step: 8 = 2.7548776662466943
# Step: 9 = 2.754877666246692
# Step: 10 = 2.7548776662466943
# Step: 11 = 2.754877666246692
# Step: 12 = 2.7548776662466943
# Step: 13 = 2.754877666246692
# Step: 14 = 2.7548776662466943
