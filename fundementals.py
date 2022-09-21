age =  0
name = 'Charlie'
bo = False

print(age)
print(name)
print(bo)


if(age > 10):
    print('That is larger than 10')
else:
    print('That is not larger than 10')


if(age < 0 and bo == True):
    print('Negative and True')
elif(age > 0 and bo == False):
    print('Positive and False')
elif(age > 100 or bo == True):
    print('Large or True')
else:
    print("I don't know")

animals = ['bear', 'lion', 'tiger', 'owl']
numbers = [1,2,3,4]

for animal in animals:
    print(animal)

for number in numbers:
    print('Look at this number', number)