# Necropolis #

Авторы проекта: Авлеева Ульяна и Варфоломеева Екатерина

Компьютерная игра Necropolis - аналог mario.  
*Управление в игре с клавиатуры.* 
*Размеры окна зафиксированы (нельзя изменять).*
*Отображение текущего результата во время игры на 3 уровне.*


### Распределение работы ### 
Ульяна: реализация классов в файлах first_and_second_general.py , level1, level2, map; переключение на уровни в start_window.py(select_level1(), select_level2(), select_level3())
Катя: реализация классов в файлах level3, start_window, функций в файлах game_over, successful_end, запись и изменение данных в info.txt, best_res.txt

### Описание ### 

На выбор дается 3 уровня:
- 1 легкий
- 2 повышенный уровень сложности с монстрами
- 3 на выживание

В 1 и 2 уровнях цель героя(скелета) - добраться до конца карты(а именно до могилы-креста), не упав мимо блоков вниз и не
столкнувшись с монстрами.
По ходу прохождения игроку также нужно собирать монетки.
Если игрок умирает(падает мимо блоков), то собранные монеты обнуляются, и уровень придется проходить заново.
Каждый уровень сопровождает фоновая музыка.

В 3 уровне цель героя - убивать падающие на него могилы прыжками на них.
Если игроку не удастся прыгнуть на могилу, то она его убьет.
В этом уровне нет конца и пользователь играет до тех пор, пока его не убьют.
Тогда уровень завершится, после чего появится результат (количество убитых могил).
Скорость спавна могил увеличивается с каждым очком.

*Удачи!*

 

### Технологии в проекте ###

Приложение написано на языке программирования Python c использованием библиотеки pygame в стиле ООП. 
Программа реализована на работе со спрайтами. 


1 уровень:
- **Класс Tile** отрисовывает блоки.
- **Класс Coin** отрисовывает монеты.
- **Класс End** отвечает за появление могилы, при соприкосновении с которой, считается, что уровень пройден.
- **Класс Level** Основной класс уровня, в нем происходит реализация анимации и столкновений, отрисовка уровня.
- **Класс ParticleEffect** Установка компонентов, отвечающих за белую пыль при беге и прыжках в ногах главного героя.
- **Класс Player** Управление героем, его анимирование, прыжки, завершение игры при выходе за границы экрана.
![](/data/first1_level_screen.png?raw=true)


2 уровень(аналогично 1 уровню):
- **class Monstr** отвечает за монстров
![](/data/second2_level_screen.png?raw=true)


3 уровень:  
**Класс Sprites** описаны все переменные и функции для всех спрайтов уровня.  
**Класс Player** управление героем.  
Метод draw_main отрисовывает землю и фон.  
Метод handle_input перемещает героя в зависимости от нажатых клавиш(AWSD+SPACE) и прокручивает землю исходя от положения скелета.

**Класс Tomb** спавн могил(врагов) рандомно(либо слева, либо справа).
Метод main - запуск основного цикла уровня(также там происходит подсчет и отрисовка очков,
перезапуск без необходимости заново запускать игру или снова выбирать уровень).
![](/data/third3_level_screen.png?raw=true)

#Все необходимые ресурсы хранятся в папке data. Результаты игры и монеты хранятся в текстовых файлах best_res.txt и info.txt  


### Техническое описание проекта ###
Для запуска приложения необходимо запустить файл (start_window.py)   

