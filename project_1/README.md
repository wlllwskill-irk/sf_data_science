# Проект 1. Анализ резюме из HeadHunter
# Модуль PYTHON-8. Инструменты для Data Science

## Оглавление

[1. Описание проекта](README.md#Описание-проекта)

[2. Какой кейс решаем?](README.md#Какой-кейс-решаем?)

[3. Краткая информация о данных](README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](README.md#этапы-работы-над-проектом)

[5. Результат](README.md#Результат)    

[6. Выводы](README.md#Выводы) 



### Описание-проекта

Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе. Проект подготавливает данные компании для построения модели.

:arrow_up:[к оглавлению](README.md#Оглавление)

### Какой кейс решаем?
Часть соискателей не указывает желаемую заработную плату, когда составляет своё резюме.
Это является помехой для рекомендательной системы HeadHunter, которая подбирает соискателям список наиболее подходящих вакансий, а работодателям — список наиболее подходящих специалистов. Прежде чем построить модель, данные необходимо преобразовать, исследовать и очистить. 

**Метрика качества**
10 баллов (из них 8 баллов — за основное задание и 2 балла — за дополнительное) за выводы по разведывательному анализу.

**Что практикуем**
Пробуем свои навыки в реальном Data Science-проекте

:arrow_up:[к оглавлению](README.md#Оглавление)

### Краткая информация о данных

1. Используется база резюме, выгруженная с сайта поиска вакансий hh.ru
   Файл можно скачать [здесь](https://drive.google.com/file/d/1CFl6yh3foRojBLOTyH3-hw2J_wIrjDEu/view?usp=sharing)
2. Используется файл с курсом валют за период, используемый в резюме.
   Файл можно скачать [здесь](https://drive.google.com/file/d/1nlVVD-uzECq9qzrxwmcXEp2KHfUBs9W1/view?usp=sharing)
  
:arrow_up:[к оглавлению](README.md#Оглавление)


### Этапы работы над проектом  
Проект будет состоять из четырёх частей:

1. **Базовый анализ структуры данных:**
- Считывание датасета
- Проверка целостности данных
- Ознакомление с признаками и их структурой
- Ознакомление с наполненностью данных
- Просмотр основной статистической информации о столбцах

2. Преобразование данных

- Разбивка признака "Образование и ВУЗ"
- Разбивка признака "Пол, возраст"
- Преобразование признака "Опыт работы"
- Разбивка признака "Город, переезд, командировки"
- Преобразование для признаков "Занятость" и "График"
- Преобразование признака заработной платы "ЗП" 


3. Разведывательный анализ

- Анализ распределения признака "Возраст"
- Анализ распределения признака "Опыт работы (месяц)"
- Анализ распределения признака "ЗП (руб)"
- Анализ зависимости признака "ЗП (руб)" от "Образование"
- Анализ распределения признака "ЗП (руб)" в зависимости от "Город"
- Анализ зависимости признака "ЗП (руб)" от признаков "Готовность к переезду" и "Готовность к командировкам"
- Анализ зависимости признака "ЗП (руб)" от признаков "Возраст" и "Образование"
- Анализ зависимости признака "Опыт работы (месяц)" от "Возраст"

Дополнительно:
- Анализ взаимосвязи опыта работы и заработной платы в зависимости от пола соискателя
- Анализ предпочтений графика работы у соискателей

4. Очистка данных
- Поиск и удаление полныех дубликатов
- Поиск пропусков в столбцах данных
- Удаление незначительного количества строк с пропусками в столбцах "Опыт работы (месяц)" и "Последняя/нынешняя должность". Заполнение пропусков в столбце "Опыт работы (месяц)" медианными значениями
- Удаление выбросов в ручную
- Удаление выбросов где опыт работы в годах превышал возраст соискателя
- Анализ и удаление выбросов с помощью метода z-отклонений


:arrow_up:[к оглавлению](README.md#Оглавление)


### Результаты:  

- Преобразованны признаки из 12 столбцов в 23
- Удалены выбросы
- Количество записей в датасете до очистки - 44744. После очистки - 44482


:arrow_up:[к оглавлению](README.md#Оглавление)


### Выводы:  

Набор данных компании подготовлен для построения модели.



:arrow_up:[к оглавлению](README.md#Оглавление)


Буду рад, если информация по этому проекту покажется вам интересной или полезной.