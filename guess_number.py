from random import randint

number = randint(1, 100)
print("Угадайте число от 1 до 100")
while True:
    guess = int(input('Введите число '))
    if guess == number:
        print("Число угадано")
        break
    if guess < number:
        print("Ваше число меньше того, что задагадо")
    else:
        print("Ваше число больше того, что задагадо")
        