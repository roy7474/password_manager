master_pwd = input('What is the master password? ')

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')

while True:
    mode = input('Would you like to add a new password or vew existing ones (view / add)? Press Q to quit ')
    if mode == 'q':
        break

    elif mode == 'view':
        view()

    elif mode == 'add':
        add()

    else:
        print('Invalid mode.')
        continue

