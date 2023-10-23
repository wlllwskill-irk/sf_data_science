"""Игра угадай число"""
import numpy as np

number = np.random.randint(1, 101) # Загадываем число

count = 0
number_min = 1
number_max = 100
while True:
    
    count +=1
    print(f"Попытка номер: {count}")
    
    # predict_number = int(input(f"Угадай число от {number_min} до {number_max}:"))
    predict_number = int(input(f"Угадай число от {number_min} до {number_max}:"))
    
    if predict_number > number:
        number_max = predict_number
        print(f"Число должно быть меньше {str(predict_number)}")
    elif predict_number < number:
        print(f"Число должно быть больше {str(predict_number)}")
        number_min = predict_number
    else:
        print(f"Поздравляем Вы угадали! Число - {str(number)} за {str(count)} попыток!")
        break
    