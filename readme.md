# Цели практической работы 
- Создать и запустить Django-приложение.
- По очереди описать модели.
- Сгенерировать и выполнить миграции для созданных моделей (по отдельности).
- Создать связи между таблицами.
- Создать веб-страницы на основе Django-шаблонов.
- Вывести на страницу сущности из базы данных.
# Что нужно сделать
1. - [x] Проект mysite.
2. - [x] Приложение shopapp.
3. - [x] Приложение, установленное в настройках.
4. - [x] Модель Product с полями типов:
    - - [x] CharField;
    - - [x] TextField;
    - - [x] DecimalField;
    - - [x] PositiveSmallIntegerField;
    - - [x] DateTimeField;
    - - [x] BooleanField.
5. - [x] Модель Order с полями типов:
    - - [x] TextField;
    - - [x] CharField;
    - - [x] DateTimeField;
    - - [x] ForeignKey — связь с моделью User;
    - - [x] ManyToManyField — связь с моделью Product.
6. - [x] Выполнение стандартных миграций.
7. - [x] Отдельные миграции для каждой из моделей.
8. - [x] Пользователя через createsuperuser.
9. - [x] View функции:
    - - [x] для shop index (список ссылок на доступные страницы);
    - - [x] для products list (список продуктов);
    - - [x] для orders list (список заказов с загруженными пользователями и продуктами).
10. - [x] Подключение view функций через urls.py внутри приложения