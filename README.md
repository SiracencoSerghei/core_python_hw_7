Репозиторій для домашнього завдання до модуля 7 (Створення та встановлення власних пакетів, віртуальне оточення)

Завдання У цьому домашньому завданні ми зробимо із скрипта розбору папки Python-пакет та консольний скрипт, який можна викликати у будь-якому місці системи з консолі командою clean-folder. Для цього вам треба створити структуру файлів та папок:

├── clean_folder 
    ├── clean_folder │ 
       ├── clean.py 
       └── init.py 
    └── setup.py

У clean_folder/clean_folder/clean.py треба помістити все, що ми зробили на попередніх домашніх завданнях по розбору папки. Ваше основнє завдання написати clean_folder/setup.py, щоб вбудований інструментарій Python міг встановити цей пакет та операційна система могла використати цей пакет як консольну команду.