import math
import random


# максимальное число попыток для угадывания числа
def number_of_attempts(num):
    return math.ceil(math.log2(num + 1))


# проверка, что введено положительное число
def is_valid(num):
    try:
        num = int(num)
        return num >= 0    # Проверяем, что число положительное или ноль
    except ValueError:
        return False


# запуск игры
def start():
    print('Давай начнем игру! Введи интервал целых положительных чисел, в котором будешь угадывать число.')
    while True:
        left = input('Введи левую границу: ')
        right = input('Введи правую границу: ')

        if is_valid(left) and is_valid(right):
            left, right = int(left), int(right)
            if left != right:
                if right < left:
                    left, right = right, left  # Меняем местами, если ввели неправильно
                break
            else:
                print('Границы должны отличаться!')
        else:
            print('Введены некорректные числа, попробуй снова.')

    guessing_game(left, right)


# определяем склонение слова
def attempt_word(attempts_needed):
    if attempts_needed % 10 == 1 and attempts_needed != 11:
        return "попытку"
    elif 2 <= attempts_needed % 10 <= 4 and not (12 <= attempts_needed % 100 <= 14):
        return "попытки"
    else:
        return "попыток"


# алгоритм игры
def guessing_game(left, right):
    num_0 = random.randint(left, right)
    attempts_needed = number_of_attempts(num_0)
    print(f'Я загадал число от {left} до {right}. Ты можешь угадать число за {attempts_needed} {attempt_word(attempts_needed)}.')

    counter = 0

    guess_on_the_first_try = ['Скажи честно, ты подглядывал?', 'Кажется, у тебя есть третий глаз!', 'Какую магию ты использовал, чтобы угадать?']
    need_higher = ['Бери выше, попробуй еще раз!', 'Введи число побольше.', 'Посмотри вверх.']
    need_lower = ['Рожденный ползать летать не может - выбери число меньше.', 'Тебе нужно спуститься пониже...', 'Попробуй число поменьше.']

    while True:
        player_num = input('Введи число.')
        if is_valid(player_num):
            counter += 1
            player_num = int(player_num)
            if player_num == num_0:
                if counter == 1:
                    print(random.choice(guess_on_the_first_try))
                else:
                    print(f'Молодец! Удача на твоей стороне, номер твоей попытки {counter}.')
                    if counter <= attempts_needed:
                        print('Ты следовал моим подсказкам и уложился в оптимальное число попыток! Молодец!')
                    else:
                        print('А вот если бы ты слушал мои подсказки, ты угадал бы число быстрее!')

                print('Спасибо, что поиграл в числовую угадайку. Еще увидимся...')

                play_again() #запускаем игру снова
                break

            elif int(player_num) < num_0:
                print(random.choice(need_higher))
            else:
                print(random.choice(need_lower))
        else:
            print('Введено некорректное число, попробуй снова.')


# предлагаем сыграть повторно
def play_again():
    while True:
        response = input('Хочешь сыграть еще раз? ').lower()
        if response in ['да', 'lf']:
            start()
            break
        elif response in ['нет', 'ytn']:
            print('Приходи, когда появится желание сыграть.')
            break
        else:
            print('Пожалуйста, ответь "да" или "нет".')


# приглашение в игру
def main():
    if input('Привет! Не желаешь сыграть в игру? Введи "да" или "нет" ').lower() in ['да', 'lf']:
        start()
    else:
        print('Приходи, когда появится желание сыграть.')


# Запуск основной функции
main()