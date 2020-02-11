import datetime

birth_year = input('What year were you born ?: ')
current_year = datetime.datetime.now().year
print(f'Current year is {current_year}')

age = current_year - int(birth_year)

print(f'So your age is {age}')
