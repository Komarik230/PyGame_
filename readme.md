# Necropolis #

Авторы проекта: Авлеева Ульяна и Варфоломеева Екатерина

Компьютерная игра Necropolis - аналог mario.  
*Управление в игре с клавиатуры.* 
*Размеры окна зафиксированы (нельзя изменять).*
*Отображение текущего результата во время игры.*

### Описание ### 

На выбор дается 3 уровня:
- 1 легкий
- 2 повышенного уровня сложности
- 3 на выживание

В 1 и 2 уровнях цель героя(скелета) - добраться до конца карты(а именно до могилы-креста), не упав мимо блоков вниз.
По ходу прохождения игроку также нужно собирать монетки.
Если игрок умирает(падает мимо блоков), то собранные монеты обнуляются, и уровень придется проходить заново.
Каждый уровень сопровождает фоновая музыка.

В 3 уровне цель героя - убивать падающие на него могилы прыжком на нее.
Если игроку не удастся прыгнуть на могилу, то она его убьет.
В этом уровне нет конца и пользователь играет до тех пор, пока его не убьют.
Тогда уровень завершится, после чего появится результат (количество убитых могил).
Скорость спавна могил увеличивается с каждым очком.

*Удачи!*

 

### Технологии в проекте ###

Приложение написано на языке программирования Python c использованием библиотеки pygame в стиле ООП. 
Программа реализована на работе со спрайтами. 


1 уровень(используются те же классы, что и для 2)

2 уровень:
**Класс Tile** отвечает за построение плиток на карте
**Класс Coin** отвечает за появление монет на карте
**Класс End** отвечает за могилу, при входе в которую считается, что уровень пройден

3 уровень:  
**Класс Sprites** описаны все переменные и функции для всех спрайтов уровня.  
**Класс PLayer** управление героем.  
Метод draw_main отрисовывает землю и фон.  
Метод handle_input перемещает героя в зависимости от нажатых клавиш(AWSD+SPACE) и прокручивает землю исходя от положения скелета.

**Класс Tomb** спавн могил(врагов) рандомно(либо слева, либо справа).
Метод main - запуск основного цикла уровня(также там происходит подсчет и отрисовка очков,
перезапуск без необходимости заново запускать игру или снова выбирать уровень).


#Все необходимые ресурсы хранятся в папке data. Цитаты и результаты игр хранятся в базе данных SQLite worm_bd.db  


### Техническое описание проекта ###
Для запуска приложения необходимо запустить файл (start_game.py?)   

(Чтобы установить все зависимости (pygame, random) 
достаточно в консоли (терминале) вызвать команду  
pip install -r requirements.txt