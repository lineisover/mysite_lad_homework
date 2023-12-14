# Цели практической работы 
- Создать и запустить Django-приложение.
- По очереди описать модели.
- Сгенерировать и выполнить миграции для созданных моделей (по отдельности).
- Создать связи между таблицами.
- Создать веб-страницы на основе Django-шаблонов.
- Вывести на страницу сущности из базы данных.
# Что нужно сделать
1. - [ ] Проект mysite.
2. - [ ] Приложение shopapp.
3. - [ ] Приложение, установленное в настройках.
4. - [ ] Модель Product с полями типов:
    - - [ ] CharField;
    - - [ ] TextField;
    - - [ ] DecimalField;
    - - [ ] PositiveSmallIntegerField;
    - - [ ] DateTimeField;
    - - [ ] BooleanField.
5. - [ ] Модель Order с полями типов:
    - - [ ] TextField;
    - - [ ] CharField;
    - - [ ] DateTimeField;
    - - [ ] ForeignKey — связь с моделью User;
    - - [ ] ManyToManyField — связь с моделью Product.
6. - [ ] Выполнение стандартных миграций.
7. - [ ] Отдельные миграции для каждой из моделей.
8. - [ ] Пользователя через createsuperuser.
9. - [ ] View функции:
    - - [ ] для shop index (список ссылок на доступные страницы);
    - - [ ] для products list (список продуктов);
    - - [ ] для orders list (список заказов с загруженными пользователями и продуктами).
10. - [ ] Подключение view функций через urls.py внутри приложения