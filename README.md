# Проект LMS-системы, бэкенд-сервер. 
В приложении используются:
- фреймворк Django
- надстройка DRF для Django
- база данных postgresql



# Для запуска проекта. 

1. Создаем базу данных в postgresql. Заходим в терминал/командную строку и вводим команды: 
   - psql -U postgres   # posgres - это имя пользователя для доступа в бд
   - create database my_data;  # my_data - имя будущей базы данных, имя можно любое(команда может с первого раза не сработать)
2. Заполняем переменные среды. В корне проекта нужно создать файл ".env" и заполнить следующие поля.
   - SECRET_KEY -     # ваш секретный ключ для приложения
   - NAME=your_data_base_name     # имя базы данных
   - USER=postgres     # имя пользователя в postgresql по дефолту postgres
   - PASSWORD=your_password     # пароль для пользователя postgresql
3. Рекомендуется заполнить БД данными из фикстур командами в следующем порядке:
   - python3 manage.py loaddata users
   - python3 manage.py loaddata lms

# Запускаем Docker Compose.
   - Командой в терминале docker-compose build собираем образ
   - Командой в терминале  docker-compose up запускаем контейнеры
