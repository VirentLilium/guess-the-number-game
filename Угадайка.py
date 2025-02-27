import math
import random


# максимальное число попыток для угадывания числа
def number_of_attempts(num):
    return math.ceil(math.log2(num + 1))


# проверка, что введено число (работает и с отрицательными числами)
def is_valid(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False


# запуск игры
def start():
    print('Давай начнем игру! Введи интервал, в котором будешь угадывать число.')
    while True:
        left = input('Введи левую границу: ')
        right = input('Введи правую границу: ')

        if is_valid(left) and is_valid(right):
            left, right = int(left), int(right)
            if left != right:
                break
            else:
                print('Границы должны отличаться!')
        else:
            print('Введены некорректные числа, попробуй снова.')
    guessing_game(left, right)


# определяем склонение слова
def attempt_word(n):
    n = number_of_attempts(n)
    if 11 <= n % 100 <= 14:
        return "попыток"
    elif n % 10 == 1:
        return "попытку"
    elif 2 <= n % 10 <= 4:
        return "попытки"
    else:
        return "попыток"


# алгоритм игры
def guessing_game(left, right):
    if right < left:
        left, right = right, left  # Меняем местами, если ввели неправильно
    num_0 = random.randint(left, right)
    attempts_needed = number_of_attempts(num_0)

    if right > 0 and left > 0:
        print(f'Я загадал число от {left} до {right}. Ты можешь угадать число за {attempts_needed} {attempt_word(attempts_needed)}.')
    else:
        print(f'Я загадал число от {left} до {right}.')
    counter = 0
    while True:
        player_num = input('Введи число.')
        if is_valid(player_num):
            counter += 1
            player_num = int(player_num)
            if player_num == num_0:
                if counter == 1:
                    print('Скажи честно, ты подглядывал?')
                    if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                        start()
                    else:
                        print('Приходи, когда появится желание сыграть снова :)')
                        break
                else:
                    print(f'Молодец! Удача на твоей стороне, номер твоей попытки {counter}.')
                    break
            elif int(player_num) < num_0:
                print('Бери выше, попробуй еще раз!')
            else:
                print('Рожденный ползать летать не может - выбери число поменьше.')
        else:
            print('Введено некорректное число, попробуй снова.')
    print('Спасибо, что поиграл в числовую угадайку. Еще увидимся...')
    play_again()


# предлагаем сыграть повторно
def play_again():
    if input('Хочешь сыграть еще раз? ').lower() in ['да', 'lf']:
        start()
    else:
        print('Приходи, когда появится желание сыграть.')


# приглашение в игру
if input('Привет! Не желаешь сыграть в игру? Введи "да" или "нет" ').lower() in ['да', 'lf']:
    start()
else:
    print('Приходи, когда появится желание сыграть.')