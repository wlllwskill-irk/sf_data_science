import numpy as np

def game_core_v1(number):
    '''Просто угадываем на ramdom ни как не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict:
            print(count)
            break
    return count # Возвращаем счетчик


def score_game():
    '''Запускаем игру 1000 раз, чтоб узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1) # фирсируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for index_number, number in enumerate(random_array):
        print(f'Угадываем число номер: {index_number}')
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')


            
if __name__ == '__main__':
    score_game()    