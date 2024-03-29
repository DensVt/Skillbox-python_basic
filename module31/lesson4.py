import itertools

colors = ['красный', 'синий', 'зеленый', 'желтый']
for item in itertools.permutations(colors, 4):
    print(item)
print('=' * 50)

for item in itertools.combinations(colors, 2):
    print(item)
print('=' * 50)

my_cycle = itertools.cycle(['one', 'two', 'three'])
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
