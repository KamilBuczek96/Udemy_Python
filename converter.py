from currency_converter import CurrencyConverter

amount = input('Podaj ilość pieniędzy: ')
currency_from  = input('Podaj walutę z której chcesz zamienić: ')
currency_to = input('Podaj walute na jaką chcesz zamienić: ')


c = CurrencyConverter()
result = round(c.convert(float(amount), currency_from, currency_to), 2)

print(f'{amount} {currency_from} to {result} {currency_to}')



