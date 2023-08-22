name = input("")
salary= int(input())

if name == 'Alice':
    print('Hey there!')

    if salary < 10000:
        print('Sounds good.')
    else:
        print("Let's discuss this a little.")
else:
    print("I don't know you.")