<h2>Тесты для утилиты grep.</h2>

Для запуска тестов должен быть установлен Pytest.

<code>pip3 install pytest</code>

Загрузка pytest_test_grep.

<code>git clone https://github.com/Devllench/pytest_test_grep.git</code>

Запуск тестов.

<code>cd pytest_test_grep</code>

<code>python3 -m pytest -v test_grep_all_case.py  test_grep_users_case.py</code>

test_grep_all_case.py - проверяет все параметры grep. Тест считается пройденным, если мы получаем ожидаемую длину вывода команды.

test_grep_users_case.py - проверяет наиболее часто используемые параметры. Тест считается пройденным, если мы получаем ожидаемый код завершения команды.

Тесты коректно отработали в окружении:
Python 3.8-3.9,Ubuntu 9
