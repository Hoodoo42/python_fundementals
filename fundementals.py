from concurrent.futures.process import _check_system_limits


age = 0
name = 'Charlie'
bo = False

print(age)
print(name)
print(bo)


if (age > 10):
    print('That is larger than 10')
else:
    print('That is not larger than 10')


if (age < 0 and bo == True):
    print('Negative and True')
elif (age > 0 and bo == False):
    print('Positive and False')
elif (age > 100 or bo == True):
    print('Large or True')
else:
    print("I don't know")

animals = ['bear', 'lion', 'tiger', 'owl']
numbers = [1, 2, 3, 4]

for animal in animals:
    print(animal)

for number in numbers:
    print('Look at this number', number)


def static_greeting():
    print('Hello Colleen')


static_greeting()


def dynamic_greeting(real_name):
    print('Hello', real_name)


real_name = 'Bob'
dynamic_greeting(real_name)

real_name = 'Katy'
dynamic_greeting(real_name)

real_name = 'Rick'
dynamic_greeting(real_name)


def find_treasure(strings):
    for buried in strings:
        if (buried == 'treasure'):
            print('Treasure Found!')
            return True

    print('No treasure')
    return False


chest_one = ['sand', 'water', 'treasure']
find_treasure(chest_one)

chest_two = ['tree', 'cave', 'sky']
find_treasure(chest_two)
