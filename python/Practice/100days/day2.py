print('Welcome to the tip calculator!')
amount = float(input('What is total bill amount\n$: '))
tip = float(input('How much tip would you like to give\nPercent: '))
people = int(input('Number of people\nPeople: '))
print(f'Each person should pay: {round((amount + amount*tip/100)/people,2)} people')