num = int(input('Введите число: '))


def fizz_buzz(num):
    for i in range(1, num + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


fizz_buzz(num)
