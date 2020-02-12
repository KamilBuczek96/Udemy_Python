login = input('Login: ')
password = input('Password: ')

password_size = len(password)
secret_password= password_size * '*'
print(f'Hello {login}, your password {secret_password} is {password_size} letters long')